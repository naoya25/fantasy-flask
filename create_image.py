from diffusers import StableDiffusionPipeline
from typing import Tuple


def create_image(prompt: str, file_name: str = "result.png") -> Tuple[bool, str]:
    try:
        pipe = StableDiffusionPipeline.from_single_file("./models/AnythingV5V3_v5PrtRE.safetensors")
        pipe.to("mps")  # windowsはcuda、macはmps

        if pipe.safety_checker is not None:
            pipe.safety_checker = lambda images, **kwargs: (images, None)
        pipe.enable_attention_slicing()

        image = pipe(prompt, width=512, height=512, num_inference_steps=20).images[0]
        image.save(f"static/images/{file_name}")
        return True, file_name
    except Exception as e:
        return False, str(e)


if __name__ == "__main__":
    prompt = "(((super realistic))), (((best quality))),((masterpiece)), ((ultra-detailed)), starry sky,  a man, smile, (((super realistic silver hair))), shirt, blue eyes, an anime style"
    print(create_image(prompt=prompt))
