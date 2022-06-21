

# Copy and paste this into python3 shell when cd'd into main neox pathway to use chat_with_gpt()

from megatron.utils import print_rank_0, setup_for_inference_or_eval

from megatron.text_generation_utils import (
    generate_samples_input_from_file,
    generate_samples_from_prompt,
    generate_samples_unconditional,
    generate_samples_interactive,
)


# Load model
model, neox_args = setup_for_inference_or_eval(use_cache=True)


# Wrapper
def chat_with_gpt(text):

	sample_generated = generate_samples_from_prompt(
	            neox_args=neox_args,
	            model=model,
	            text=text,
	            recompute=neox_args.recompute,
	            temperature=neox_args.temperature,
	            maximum_tokens=neox_args.maximum_tokens,
	            top_k=neox_args.top_k,
	            top_p=neox_args.top_p,
        )
	print(f'sample_generated: {sample_generated}')


# Example
chat_with_gpt("Anuj was having a lovely Day")

