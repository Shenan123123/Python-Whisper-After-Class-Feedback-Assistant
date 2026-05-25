from faster_whisper import WhisperModel

# 加载模型
model = WhisperModel(
    "small",
    device="cpu"
)


# 转录函数
def transcribe_audio(audio_path):

    segments, info = model.transcribe(
        audio_path,
        language="zh"
    )

    result = ""

    for segment in segments:
        result += segment.text + "\n"

    return result


# 测试代码
if __name__ == "__main__":

    text = transcribe_audio("audio/test.m4a")

    print(text)

    with open(
        "output/result.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(text)