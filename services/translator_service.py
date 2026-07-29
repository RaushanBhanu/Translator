from googletrans import Translator


async def translate(text: str, src: str | None = None, dest: str = "en"):
    async with Translator() as translator:
        if src:
            return await translator.translate(
                text,
                src=src,
                dest=dest,
            )

        return await translator.translate(
            text,
            dest=dest,
        )
