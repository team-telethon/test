from telethon import TelegramClient, client, events
from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.input_stream.quality import HighQualityVideo
from iqthon import iqthon
import asyncio


iqthon_py = PyTgCalls(iqthon)
iqthon_py.start()


YoutubeLink = 'https://www.youtube.com/watch?v=8lUroR3MmAs'
# USE THIS IF YOU WANT SYNC WAY
async def get_youtube_stream():
    # USE THIS IF YOU WANT ASYNC WAY
    async def run_async():
        proc = await asyncio.create_subprocess_exec(
            'youtube-dl',
            '-g',
            '-f',
            # CHANGE THIS BASED ON WHAT YOU WANT
            'best[height<=?360][width<=?640]',
            YoutubeLink,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        stdout, stderr = await proc.communicate()
        return stdout.decode().split('\n')[0]
    link = await run_async()
    return link

async def JoinThenStream():
    await iqthon_py.join_group_call(
        chat_id,
        AudioVideoPiped(
            StreamLink,
            HighQualityAudio(),
            HighQualityVideo(),
        ),
        stream_type=StreamType().pulse_stream,
    )


# DOWNLOAD THEN STREAM
@iqthon.on(events.NewMessage(outgoing=True, pattern=r'PlayThis ?(.*)'))
async def YoutubeToVoiceChat(event):
    global YoutubeLink, StreamLink, chat_id

    chat = await event.get_chat()
    chat_id = '-100'+str(chat.id)

    YoutubeLink = str(event.text).replace('PlayThis', '').strip()
    order = await event.edit(f'STREAMING WILL START SOON : {YoutubeLink}')
    StreamLink = await get_youtube_stream()
    StartStreaming = await JoinThenStream()
    order = await event.edit(f'STREAMING STARTED NOW : {YoutubeLink}')


idle()

