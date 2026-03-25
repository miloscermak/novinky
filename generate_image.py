#!/usr/bin/env python3
"""
Generátor ilustrací pro Explainer články.
Používá Google Gemini API pro generování obrázků.

Použití:
    python generate_image.py "popis scény" output.png
    python generate_image.py "popis scény" output.png --model gemini-2.5-flash-image
    python generate_image.py "popis scény" output.png --raw --aspect 16:9

Modely:
    gemini-2.5-flash-image  (default, doporučený)
    imagen-4.0-generate-001 (Imagen 4)

API klíč se čte z .env souboru (GEMINI_API_KEY=...) nebo z env proměnné.
Skript automaticky přidává stylový prefix (New Yorker cartoon) — pro čistý prompt použij --raw.
"""

import argparse
import base64
import sys
import os
from pathlib import Path

# Načti .env ze stejné složky jako skript
from dotenv import load_dotenv
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

from google import genai
from google.genai import types


DEFAULT_MODEL = "gemini-2.5-flash-image"

# Výchozí styl pro Explainer ilustrace
DEFAULT_STYLE_PREFIX = (
    "Black and white ink drawing in the style of a New Yorker magazine cartoon. "
    "Clean lines, minimal detail, witty editorial illustration style. "
    "One subtle pastel accent color. No caption text. "
)


def generate_image(
    prompt: str,
    output_path: str,
    model: str = DEFAULT_MODEL,
    use_default_style: bool = True,
    aspect_ratio: str = "1:1",
):
    """Vygeneruje obrázek a uloží ho do souboru."""

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Chyba: GEMINI_API_KEY není nastaven.")
        print(f"Vytvoř soubor {env_path} s obsahem:")
        print("  GEMINI_API_KEY=tvůj_klíč_z_ai.google.dev")
        sys.exit(1)

    # Přidej výchozí styl, pokud je zapnutý
    full_prompt = DEFAULT_STYLE_PREFIX + prompt if use_default_style else prompt

    print(f"Model: {model}")
    print(f"Prompt: {full_prompt[:120]}...")
    print(f"Aspect ratio: {aspect_ratio}")
    print("Generuji...")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model,
        contents=full_prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            response_mime_type="image/png",
        ),
    )

    # Najdi obrázek v odpovědi
    image_saved = False
    for part in response.candidates[0].content.parts:
        if part.inline_data and part.inline_data.mime_type.startswith("image/"):
            image_data = part.inline_data.data
            # Pokud jsou data base64 string, dekóduj
            if isinstance(image_data, str):
                image_data = base64.b64decode(image_data)

            with open(output_path, "wb") as f:
                f.write(image_data)

            size_kb = len(image_data) / 1024
            print(f"Uloženo: {output_path} ({size_kb:.0f} KB)")
            image_saved = True
            break

    if not image_saved:
        print("Chyba: API nevrátilo obrázek.")
        print(f"Odpověď: {response.text if hasattr(response, 'text') else response}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Generátor ilustrací pro Explainer (Gemini API / Nano Banana)"
    )
    parser.add_argument("prompt", help="Popis obrázku k vygenerování")
    parser.add_argument(
        "output",
        nargs="?",
        default="ilustrace.png",
        help="Výstupní soubor (default: ilustrace.png)",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Gemini model (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Nepoužívat výchozí New Yorker styl, jen čistý prompt",
    )
    parser.add_argument(
        "--aspect",
        default="1:1",
        choices=["1:1", "16:9", "9:16", "4:3", "3:4"],
        help="Poměr stran (default: 1:1)",
    )

    args = parser.parse_args()

    generate_image(
        prompt=args.prompt,
        output_path=args.output,
        model=args.model,
        use_default_style=not args.raw,
        aspect_ratio=args.aspect,
    )


if __name__ == "__main__":
    main()
