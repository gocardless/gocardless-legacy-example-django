from django.shortcuts import render, redirect
import gocardless

gocardless.environment = "sandbox"

gocardless.set_details(app_id="kzCOPw2JtJvRQxKTlFqQTGvxLvkoMS1Eb0Dgl5QVc1W0NKpOEZDvESfGOI_kkG2l",
    app_secret="IO9AlgPsbYNCtFlciV_HOBrGB3Mi07PFYSn2zx4uK5xaWJI1AzwnYeC86x46ji_g",
    token="5EFkzOrUOZ8t+iaP86NggIy+iKGJ0f7QMnMd+Q3P4mQk17Kzq9G1vYrNlEWFldlg",
    merchant_id="02FX1YS3H1"})

def index(request):
    subscriptions = gocardless.client.merchant().subscriptions()
    return render(request, "index.html", {"subscriptions":subscriptions})

def create_bill(request):
    url = gocardless.client.new_bill_url(2.99, 
        name="Domain Registration")
    return redirect(url)

def create_subscription(request):
    url = gocardless.client.new_subscription_url(99, 1, "month", 
            name="Dedicated Server Subscription",
            description="Dedicated server with quad core and 8GB of RAM")
    print(url)
    return redirect(url)

def create_preauth(request):
    max_amount = int(request.POST["budget"])
    url = gocardless.client.new_preauthorization_url(max_amount, 1, "month",
            name="Variable Priced Hosting",
            description="With our cloud-based hosting means you'll only be" 
                "charged for the resouces you use. Your charge will be" 
                "capped at {0} GBP.".format(max_amount))
    return redirect(url)

def create_preauth_bill(request):
    amount = request.POST["amount"]
    preauth_id = request.POST["preauth-id"]
    preauth = gocardless.resources.PreAuthorization.find(preauth_id)
    preauth.create_bill(amount, name="Variable Hosting Charge")

def success(request):
    gocardless.client.confirm_resource(request.GET)
    return render(request, "success")

