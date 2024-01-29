import argparse
import os
import torch
import torchaudio

from extraRepos.tortoiseTTS.tortoise.api import TextToSpeech, MODELS_DIR

from extraRepos.tortoiseTTS.tortoise.utils.audio import load_voices

def perform_tts(text, voice, preset='fast'):
    use_deepspeed = torch.cuda.is_available()
    kv_cache = True
    half = True
    output_path = 'results/'
    model_dir = MODELS_DIR
    candidates = 3
    seed = None
    produce_debug_state = True
    cvvp_amount = 0.0

    os.makedirs(output_path, exist_ok=True)

    tts = TextToSpeech(models_dir=model_dir, use_deepspeed=use_deepspeed, kv_cache=kv_cache, half=half)

    selected_voices = voice.split(',')
    for k, selected_voice in enumerate(selected_voices):
        if '&' in selected_voice:
            voice_sel = selected_voice.split('&')
        else:
            voice_sel = [selected_voice]
        voice_samples, conditioning_latents = load_voices(voice_sel)
        gen, dbg_state = tts.tts_with_preset(text, k=candidates, voice_samples=voice_samples,
                                             conditioning_latents=conditioning_latents,
                                             preset=preset, use_deterministic_seed=seed,
                                             return_deterministic_state=True, cvvp_amount=cvvp_amount)
        if isinstance(gen, list):
            for j, g in enumerate(gen):
                torchaudio.save(os.path.join(output_path, f'{selected_voice}_{k}_{j}.wav'),
                                g.squeeze(0).cpu(), 24000)
        else:
            torchaudio.save(os.path.join(output_path, f'{selected_voice}_{k}.wav'),
                            gen.squeeze(0).cpu(), 24000)

        if produce_debug_state:
            os.makedirs('debug_states', exist_ok=True)
            torch.save(dbg_state, f'debug_states/do_tts_debug_{selected_voice}.pth')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, help='Text to speak.',
                        default="The expressiveness of autoregressive transformers is literally nuts! I absolutely adore them.")
    parser.add_argument('--voice', type=str, help='Selects the voice to use for generation. See options in voices/ directory (and add your own!) '
                                                  'Use the & character to join two voices together. Use a comma to perform inference on multiple voices.',
                        default='random')
    parser.add_argument('--preset', type=str, help='Which voice preset to use.', default='fast',
                        choices=['high_quality', 'standard', 'fast', 'ultra_fast'])
    args = parser.parse_args()

    perform_tts(text=args.text, voice=args.voice, preset=args.preset)
