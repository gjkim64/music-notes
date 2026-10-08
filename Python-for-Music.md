# Python for Music

[← Home](README.md)

> 출처: `Manual2.pptx` (Jython, Python Music, Anaconda), `systemsetup.txt`, `fakebass.txt`, `plot_music_sync.py`

---

## 1. Jython / jMusic (JythonMusic)

JythonMusic은 Java 기반 음악 라이브러리 **jMusic** 위에서 동작한다.

**실행 방법**
1. jython 디렉토리에서 명령 프롬프트 열기
2. `java -jar jem.jar` 실행 → 환경 창이 열림
   - 또는 jython Windows 배치 파일을 더블클릭
3. 창에 jython 프로그램을 입력하거나 붙여넣기

**주의할 점**
- 파일 이름을 지정해서 편하게 실행하는 방법은 아직 못 찾음.
- Java 기반이라 **jython으로 실행**해야 기능을 쓸 수 있다.
- Anaconda 콘솔의 python에서는 `music` 을 import할 수 없음 (✗).
- jython 안에서는 `sounddevice` 를 import할 수 없음 — Anaconda에 설치한 것이 아니라 자체 python 사본을 쓰는 듯 (✗).

## 2. Python 음악 패키지

| 패키지 | 용도 |
| :--- | :--- |
| `MIDIFile` | MIDI 파일 파싱·읽기 |
| `sounddevice` | MP3 / WAV 재생 — `sd.play(np_array, fs * scale)` |
| `soundfile` | 오디오 파일 읽기 |
| `librosa` | 온셋·템포 추정, 크로마, DTW 등 |

**정리**
- jython, sounddevice, MIDIFile을 한 환경에서 같이 쓰기는 어려울 것 같다.
- **오프라인 MIDI 처리**는 jython, **온라인 재생**은 librosa 등으로.
- librosa의 DTW가 버전 문제로 동작하지 않을 때는 `librosa.sequence.dtw` 를 쓴다 (예전 `librosa.core.dtw` 대신).

## 3. Anaconda / conda 환경

- `conda create` 로 버전을 확실하게 관리한다.
  - 최소한 **python 버전은 지정**. 나머지는 activate 후 설치·설정.
- 환경이 저장되는 디렉토리를 기록해 두고 가지고 다닌다.
- Jupyter notebook에서 kernel / environment 설정.
- PyCharm 사용.
- 설치: `pip install …` 또는 `conda install …` (❓ 매번 해야 하나?)
- python 종료: `exit()`

```bash
conda create -n music python=3.10
conda activate music
pip install librosa sounddevice soundfile
python -m ipykernel install --user --name music
```

---

## 4. 예제 코드

### 4.1 DTW 음악 동기화 — [`code/plot_music_sync.py`](code/plot_music_sync.py)

librosa 갤러리 예제 (Stefan Balke, ISC License). 템포가 다른 두 녹음 (Stevie Wonder *Sir Duke* 브라스 리크, 약 7초 / 5초)을 정렬한다.

1. 두 오디오 로드
2. **크로마 특징** 추출 (`n_fft=4410`, `hop=2205`)
3. **DTW** 로 정렬 경로(warping path) 계산 (cosine metric)
4. 누적 비용 행렬 위에 경로 표시, 시간 영역에서 대응점을 빨간 선으로 연결

> 활용: 같은 곡의 다른 녹음 사이를 오가는 플레이어, 느린 녹음을 빠른 템포에 맞추는 time-scale modification.
> 참고문헌: Meinard Müller, *Fundamentals of Music Processing*, Springer, 2015.
> 최신 librosa에서는 `librosa.display.waveplot` → `waveshow`, `librosa.core.dtw` → `librosa.sequence.dtw` 로 바뀌었다.

### 4.2 FakeBass 실험 스케치 — [`code/fakebass_sketches.py`](code/fakebass_sketches.py)

- WAV를 10개 구간으로 나누어 `sounddevice` 로 재생
- 재생하는 동안 다른 스레드에서 현재 시간을 출력 (재생과 동기화 테스트)
- librosa로 온셋 강도 → 템포 추정 (균등 prior 30–300 BPM, 동적 템포)

```python
y, sr = librosa.load('super.wav', duration=30)
onset_env = librosa.onset.onset_strength(y=y, sr=sr)
tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
```
