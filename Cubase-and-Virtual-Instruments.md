# Cubase & Virtual Instruments

[← Home](README.md)

> 출처: `music-mar22.pptx` (Cubase SX, Battery 슬라이드)

---

## 1. Cubase SX 기본 셋업

1. **Device setup**: 오디오 카드로 보내는 설정을 먼저 한다.
2. **VST Instrument** 선택
3. **Track 추가**: 빈 곳 더블클릭
   - In: *All MIDI inputs* → 확인: Play bar 오른쪽 게이지 (빨강)
   - Out: 가상악기 (예: HyperCanvas) → 확인: Play bar 오른쪽 게이지 (초록)
4. 채널별로 악기 선택

## 2. 단축키

| 키 | 기능 |
| :--- | :--- |
| G / H | Time scale 확대·축소 |
| Ctrl/Alt + 숫자 | 구간 지정 |
| Ctrl+D | 단순 복사 (바로 오른쪽에 반복) |
| Alt+클릭 후 이동 | 응용 복사 (원하는 곳으로) |
| Ctrl+K | 대량 복사 (Edit → Repeat) |
| Ctrl+Z / Ctrl+Shift+Z | Undo / Redo |
| J | Snap 켜기·끄기 |
| Space | Play / Stop |
| F2 | Control bar 숨기기 |
| Delete | 음 삭제 (지우개 대신) |

- Panning: 스크롤 버튼을 누른 채로 조절.

## 3. 입력 & 편집 (Input / Editing)

- **Snap (J)**: 지정된 경계선에 맞출지, 자유롭게 편집할지 선택.
- 음 길이는 연필 도구로 그냥 조절. 비슷한 음이 많으면 선택해서 한꺼번에 편집.
- 세밀한 편집은 resolution을 바꿔서. 작업할 때는 창을 최대화.

### Expressive control (왼쪽 메뉴)

| 항목 | 설명 |
| :--- | :--- |
| Velocity vs. Volume | 음색 vs. 음량. 대체로 멜로디 고음은 강하게 (90–110), 아래는 약하게 (60–80) |
| Expression | 구간의 볼륨 조절, 특히 연속된 현악기 음에 |
| Sustain | 조가 바뀌는 곳에서 잠깐 뗐다가 다시 |
| Pitch bend | 상대적 세팅 (한 음 위/아래) |
| Modulation | 비브라토. 대개 0에서 점차 증가 |

## 4. 녹음

- **메트로놈**: *Transport → Metronome* 메뉴. MIDI 음/시스템 음 선택, 클릭 음 높이 설정 가능 (대개 C#1 또는 F#1). Control bar 오른쪽 위 클릭 컨트롤 (* 표시 등).
- **템포**: Fixed 모드로 놓고 녹음.
- 녹음 후 **Over Quantize** → *Quantize ends*.
- **레이어 하나씩 추가**: Control bar 왼쪽에서 *Punch in* 선택 후 Play 하면서 녹음.

---

## 5. 가상악기 (Virtual Instruments)

| 악기 | 용도 / 메모 |
| :--- | :--- |
| **Battery** | WAV로 변환한 파일을 가상 악기처럼 특정 키에 매핑. WAV나 CD 음원은 SoundForge 등으로 먼저 편집 |
| **Stylus** | 한 채널 악기. 두 채널 이상 쓰려면 필요한 만큼 더 instantiate. 루프로 듣고 고른 다음 Groove control로 선택 |
| **Trilogy** | 베이스용 |
| 기타 | 특수 가상 악기들 |
