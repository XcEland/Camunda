import asyncio
from pyzeebe import ZeebeClient, create_camunda_cloud_channel, ZeebeWorker


# Define the job worker
async def my_service_task_handler(job):
    # Extract job variables
    order_id = job.variables.get("order_id")
    customer_name = job.variables.get("customer_name")

    # Print the order ID and customer name
    print(f"Order ID: {order_id}, Customer Name: {customer_name}")

    # Complete the job (optional)
    await job.complete({"status": "processed"})


async def main():
    # Create a channel to connect to Camunda Cloud
    grpc_channel = create_camunda_cloud_channel(
        client_id="-OiAG_6p4ltIFopXx_xL-O2F.J5bp3~F",
        client_secret="P6ry33WqCWLLiJMfWw6KALUtDze.ZYkFIOy3lYDoYvEDyv~FK-JQjV9vD3n.cUik",
        cluster_id="2de87ef2-4788-4f45-8021-df31cc7e51c8",
        region="ont-1",
    )
    
    zeebe_client = ZeebeClient(grpc_channel)

    # Create a worker to listen for jobs
    worker = ZeebeWorker(grpc_channel)

    # Register the service task handler with the worker
    @worker.task(task_type="print")  # Replace with your actual task type
    async def service_task(job):
        await my_service_task_handler(job)

    # Start the worker to listen for jobs
    await worker.start()  # Note: This is now needed to start listening for tasks

    print("Worker is now listening for tasks...")

    # Run a Zeebe process instance
    process_instance_key = await zeebe_client.run_process(
        bpmn_process_id="chatbot_v1",
        variables={"order_id": 1234, "customer_name": "John Doe"}  # Example variables
    )
    
    print(f"Process instance key: {process_instance_key}")

# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())
