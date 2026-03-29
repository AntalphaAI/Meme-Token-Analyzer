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
    title: 图片生成
    desc: 生成代币冲向月球的预测图
    integrations: image-generation
    """
    ctx = runtime.context
    
    try:
        # 初始化图片生成客户端
        client = ImageGenerationClient(ctx=ctx)
        
        # 构建提示词
        prompt = f"A dynamic, high-quality photograph of a cartoon {state.token_name} character launching into space on a rocket, cinematic lighting, trending on ArtStation"
        
        logger.info(f"Generating image with prompt: {prompt}")
        
        # 生成图片
        response = client.generate(
            prompt=prompt,
            size="2K"
        )
        
        # 提取图片URL
        if response.success and response.image_urls:
            image_url = response.image_urls[0]
            logger.info(f"Image generated successfully: {image_url}")
            return ImageGenNodeOutput(generated_image_url=image_url)
        else:
            error_msg = "; ".join(response.error_messages) if response.error_messages else "Unknown error"
            logger.error(f"Image generation failed: {error_msg}")
            raise Exception(f"图片生成失败: {error_msg}")
            
    except Exception as e:
        logger.error(f"Image generation error: {str(e)}", exc_info=True)
        raise
