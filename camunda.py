import asyncio
from pyzeebe import ZeebeClient, create_camunda_cloud_channel

async def main():
    grpc_channel = create_camunda_cloud_channel( 
        client_id="-OiAG_6p4ltIFopXx_xL-O2F.J5bp3~F",
        client_secret="P6ry33WqCWLLiJMfWw6KALUtDze.ZYkFIOy3lYDoYvEDyv~FK-JQjV9vD3n.cUik",
        cluster_id="2de87ef2-4788-4f45-8021-df31cc7e51c8",
        region="ont-1",
    )
    
    zeebe_client = ZeebeClient(grpc_channel)
    
    process_instance_key = await zeebe_client.run_process(
        bpmn_process_id="chatbot_v1",
        variables={"order_id": 1234, "customer_name": "John Doe"}  # Example variables
    )
    
    print(f"Process instance key: {process_instance_key}")

asyncio.run(main())
