from fastapi import APIRouter, HTTPException
import stripe

from app.core.config import settings

router = APIRouter()

stripe.api_key = settings.STRIPE_SECRET_KEY

@router.post("/create-checkout-session")
async def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'T-shirt',
                    },
                    # 'unit_amount': 2000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://google.com',
            cancel_url='https://yahoo.com',
        )
        return {"id": session.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
