import random
import time

class PaymentGateway:
    def process_payment(self, amount):
        # Simulate network issues or external service failures
        if random.random() < 0.3:  # 30% chance of failure
            raise ConnectionError("Payment gateway is temporarily unavailable.")
        # Simulate successful payment
        return {"status": "success", "transaction_id": f"txn_{int(time.time())}"}

class UserService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def attempt_purchase(self, user_id, amount):
        print(f"User {user_id} attempting to purchase for {amount}...")
        try:
            # This is the 'happy path' where everything works
            payment_result = self.payment_gateway.process_payment(amount)
            print(f"Payment successful! Transaction ID: {payment_result['transaction_id']}")
            # In a real app, you'd update user's order status here
            return True
        except ConnectionError as e:
            # This is the 'failure handling' part
            print(f"Error processing payment: {e}")
            print("Please try again later or contact support.")
            # In a real app, you might queue this for retry, notify admin, or show a user-friendly message
            return False
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            return False

# --- Simulation ---

# Initialize the payment gateway (could be a real external service)
payment_gateway = PaymentGateway()

# Initialize the user service, injecting the payment gateway
user_service = UserService(payment_gateway)

# Simulate a few purchase attempts
print("--- Simulating Purchases ---")
for i in range(5):
    success = user_service.attempt_purchase(f"user_{i+1}", 100.00)
    if not success:
        print(f"Purchase attempt {i+1} failed.")
    print("--------------------")
    time.sleep(1) # Small delay between attempts

print("Simulation finished.")
