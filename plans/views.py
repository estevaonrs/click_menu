import datetime
from django.shortcuts import render
from .forms import PagamentoForm
from asaas.payments import CreditCard, CreditCardHolderInfo, BillingType
from datetime import date
from asaas import Asaas, Customer
from .models import Plano
from django.shortcuts import render, get_object_or_404


def GeralPlans(request):
    plans = Plano.objects.all()
    context = {
        'plans': plans,
    }
    return render(request, 'plan.html', context)


def plano_detail(request, plano_id):
    plano = get_object_or_404(Plano, pk=plano_id)
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            nome_cliente = form.cleaned_data['nome_cliente']
            cpf_cnpj = form.cleaned_data['cpf_cnpj']
            numero_cartao = form.cleaned_data['numero_cartao']
            mes_validade = form.cleaned_data['mes_validade']
            ano_validade = form.cleaned_data['ano_validade']
            ccv = form.cleaned_data['ccv']
            email = form.cleaned_data['email']
            endereco = form.cleaned_data['endereco']
            cep = form.cleaned_data['cep']
            telefone = form.cleaned_data['telefone']

            # Create an instance of the Asaas library
            asaas = Asaas(access_token='$aact_YTU5YTE0M2M2N2I4MTliNzk0YTI5N2U5MzdjNWZmNDQ6OjAwMDAwMDAwMDAwMDAwNTY3MzI6OiRhYWNoXzMzMzAzZDY2LTA3YTUtNDJhNi1iYzRjLTAwYzNkYjEwOWI0MA==', production=False)

            # Verify if the customer already exists based on CPF/CNPJ
            existing_customers = asaas.customers.list(cpfCnpj=cpf_cnpj)

            if len(existing_customers) > 0:
                # Customer already exists, use the existing customer ID
                customer_id = existing_customers[0].id
            else:
                # Create a new customer
                customer_id = None

            now = date.today()
            date_created = now.strftime("%Y-%m-%d")

            if customer_id is None:
                new_customer = asaas.customers.new(
                    name=nome_cliente,
                    email=email,
                    cpfCnpj=cpf_cnpj,
                    postalCode=cep,
                    addressNumber=endereco,
                    phone=telefone
                )
                customer_id = new_customer.id

            credit_card = CreditCard(
                holderName=nome_cliente,
                number=numero_cartao,
                expiryYear=ano_validade,
                expiryMonth=mes_validade,
                ccv=ccv
            )

            credit_card_holder_info = CreditCardHolderInfo(
                name=nome_cliente,
                email=email,
                cpfCnpj=cpf_cnpj,
                postalCode=cep,
                addressNumber=endereco,
                addressComplement='',
                phone=telefone
            )

            customer = Customer(
                id=customer_id,
                dateCreated=date_created,
                name=nome_cliente,
                cpfCnpj=cpf_cnpj
            )
            valor_plano = float(plano.valor)


            pagamento = asaas.payments.new(
                customer=customer,
                billingType=BillingType.CREDIT_CARD,
                value=valor_plano,
                dueDate=now,
                creditCard=credit_card.json(),
                creditCardHolderInfo=credit_card_holder_info.json()
            )

            if pagamento.id:
                mensagem = "Pagamento processado com sucesso!"
            else:
                mensagem = "Falha no processamento do pagamento. Por favor, tente novamente."

            return render(request, 'pagamento.html', {'form': form, 'mensagem': mensagem})

    else:
        form = PagamentoForm()

    return render(request, 'checkout.html', {'form': form, 'plano': plano,})
