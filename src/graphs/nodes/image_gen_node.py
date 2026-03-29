import logging
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from coze_coding_dev_sdk import ImageGenerationClient
from graphs.state import ImageGenNodeInput, ImageGenNodeOutput

logger = logging.getLogger(__name__)


def image_gen_node(
    state: ImageGenNodeInput,
    config: RunnableConfig,
    runtime: Runtime[Context]
) -> ImageGenNodeOutput:
    """
    title: Image Generation
    desc: Generate a prediction image of the token launching to the moon
    integrations: image-generation
    """
    ctx = runtime.context
    
    try:
        # Initialize image generation client
        client = ImageGenerationClient(ctx=ctx)
        
        # Build prompt
        prompt = f"A dynamic, high-quality photograph of a cartoon {state.token_name} character launching into space on a rocket, cinematic lighting, trending on ArtStation"
        
        logger.info(f"Generating image with prompt: {prompt}")
        
        # Generate image
        response = client.generate(
            prompt=prompt,
            size="2K"
        )
        
        # Extract image URL
        if response.success and response.image_urls:
            image_url = response.image_urls[0]
            logger.info(f"Image generated successfully: {image_url}")
            return ImageGenNodeOutput(generated_image_url=image_url)
        else:
            error_msg = "; ".join(response.error_messages) if response.error_messages else "Unknown error"
            logger.error(f"Image generation failed: {error_msg}")
            raise Exception(f"Image generation failed: {error_msg}")
            
    except Exception as e:
        logger.error(f"Image generation error: {str(e)}", exc_info=True)
        raise
