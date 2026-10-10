# FL Studio Guide

[← Home](README.md)

> 출처: `FL-11-15` ~ `FL-11-21` 메모, `FL-changetimemaker.txt`, `FL-loop recording.txt`, `music-notes-2026-10.txt`, `Manual2.pptx`
> ❓ 표시는 원본 메모에서 아직 해결하지 못한 질문입니다.

---

## 1. 기본 옵션 & 저장

- **Options → Audio**: resample을 512로 설정하면 좋다.
- **Zipped 저장**: *Save as zipped* 로 저장하면 사용한 사운드 소스도 함께 저장되어, 나중에 다시 열 때 문제가 적다.
  - 복원: 저장된 zip 파일을 FL Studio 창 위로 드래그 앤 드롭하면 알아서 열린다.
- **Export 설정**: MP3 320 kbps, WAV 비트 깊이, quality 512.
- **MIDI 저장**: *Tools → Macros → Prepare for MIDI export* 후 저장.
- 저장 시 템포 옵션 확인.

## 2. 플러그인 / 가상악기

| 용어 | 의미 |
| :--- | :--- |
| VSTi | 가상 악기 (Virtual Instrument) |
| VST | 가상 이펙트 (Virtual Effect) |
| Stock plugin | 기본 내장 플러그인 |
| Third party | 외부 플러그인 (대체로 유료) |

- SW 악기 외에 HW 악기도 쓸 수 있으며, A/D 컨버터가 필요할 수 있다.

**플러그인 추가하기**
1. *Add* 메뉴로 이동
2. *Refresh plugin list (fast scan)* — `C:/Program Files/Steinberg/VstPlugins` 등을 스캔해서 설치
3. *Plugin database* 에서 확인
4. 플러그인을 클릭해서 DB에 추가 (이미 추가된 것처럼 보여도)

- **F8**: 플러그인 피커에서 원하는 플러그인을 트랙으로 드래그.
- Channel rack 항목을 특정 믹서 트랙으로 보내기: 선택 후 **Ctrl+L**.

## 3. 단축키 (Shortcuts)

| 키 | 기능 |
| :--- | :--- |
| F5 | Playlist / Pattern 창 |
| F6 | Channel Rack |
| F7 | Piano Roll (Channel Rack에서 대상 선택 후) |
| F8 | 설치된 Plugin 보기 |
| F9 | Mixer |
| F12 | 모든 창 닫기 |
| Ctrl+A | 전체 선택 |
| Ctrl+Shift+클릭 | 하나씩 골라 선택 |
| Ctrl+드래그 | 박스로 그룹 선택 |
| Ctrl+X | 잘라내기 / 삭제 |
| Ctrl+B | 선택 부분을 바로 옆에 복사 |
| Ctrl+Z | 마지막 작업 되돌리기 |
| Ctrl+Alt+Z | 히스토리 되돌리기 (여러 단계) |
| Ctrl+L | 선택 채널을 믹서 트랙에 연결 |

**Playlist / Pattern 창**
- **C** = 자르기 (cut), **P** = 연필 (pencil) 도구
- **Select 모드**: 선택해서 작업
- **Pencil 모드**: Shift+← → 로 이동, Ctrl+↑ ↓ 로 옥타브 이동

**Piano Roll**
- Shift+드래그: 복사해서 이동

**화면 배율**
- 가로: 스크롤바 끝을 드래그
- 세로: 창 오른쪽 위 모서리 드래그

## 4. 녹음 (Recording)

### 오디오 녹음
1. *Options → Audio settings* 에서 오디오 장치 선택 (오디오 인터페이스가 없으면 **FL Studio ASIO**)
2. Mixer 트랙을 선택하고 오른쪽에서 Input 설정
3. 빨간 Record 버튼
4. 채널 → Master 로 가는 초록 연결선을 토글해서 연결을 끊을 수 있다
5. Mixer 오른쪽 채널 슬롯을 클릭해서 이펙트 연결

### 보이스 트랙 녹음
1. Playlist에 audio track 추가
2. audio track을 mixer track에 연결
3. Mixer track 입력을 mono in 으로
4. Ready 버튼 (동그라미) → Record / Play

### MIDI 녹음 (MIDI 악기로부터)
1. 원하는 Channel Rack 채널을 선택해서 활성화
2. Piano Roll로 이동
3. Record

### 루프 녹음 (AKAI 멀티 악기)
- AKAI를 여러 악기로 쓰려면 **AKAI SW editor** 로 채널을 1, 2번 등으로 따로 설정하고 RAM으로 보낸다. RAM이므로 껐다 켜면 다시 설정해야 한다.
- FL에서 MIDI 설정으로 컨트롤러를 선택하고, 필요하면 매핑한다.
- Pattern 창에서 Ctrl+드래그로 두 채널이 모두 활성화되게 선택.
- **Quantize** 해 두면 루프 녹음이 편하다 (역삼각형 Tools 메뉴).

## 5. 템포 & 박자 (Tempo / Time Signature)

### 구간별 템포 설정 (Tempo automation)
1. Playlist에서 사각형 아이콘으로 구간 선택
2. 템포 설정
3. 템포 창 우클릭 → **Create automation clip** → 편집해서 *ritardando* 등을 만들 수 있다
4. automation의 min/max를 조정 (다른 곳에서는 pan/volume에 해당) — min 0, max ~512 BPM
5. editor 도구로 비율을 조정

- 템포는 Piano Roll에서도, automation으로도 설정할 수 있다. 둘 다 있으면 **Piano Roll 설정이 automation을 덮어쓴다**.

### 박자 바꾸기 (Change time marker)
1. Piano Roll에서 time progress marker (긴 줄의 역삼각형)를 설정
   - 해당 자리에 음표가 없으면 안 되므로, 임시 음표를 먼저 놓고 marker를 정확히 위치시킨다
2. 맨 왼쪽 역삼각형 메뉴 열기
3. **Change time marker** 로 박자 세팅

## 6. 편집 도구 (Piano Roll Tools)

| 기능 | 위치 |
| :--- | :--- |
| 코드 입력 | Piano Roll 드롭다운의 **Stamp** 도구 (한자 세 글자처럼 생긴 아이콘) |
| 코드 진행, riff, quantize, chop, arpeggiator | **Tools** (렌치 모양 드롭다운) |
| 드럼 패턴, arpeggiator, automation, chopping | 왼쪽 중간 **Scores** 메뉴 → FPC drum loop |
| 베이스 라인 변주 | Chop 도구 --> 왼쪽 Scores 밑에 Chopping 혹은 Piano Roll 위 왼쪽 Wrench 밑에 Chop tool |






## 7. 채널과 트랙 분리 (Splitting by Channel)

- Channel Rack에서 여러 악기를 각각의 채널에 두면, 이것이 Playlist의 **한 트랙**에 들어간다.
- 한 트랙을 악기별 여러 트랙으로 나누는 것이 권장되는 경우가 많다 (채널 = 악기 하나, 트랙 = 채널 하나).
- 방법: 맨 왼쪽의 **패턴 이름 클릭 → Split by channel**

## 8. 오디오 클립을 다른 템포에 맞추기

MIDI 등 템포가 다른 것에 오디오 클립을 맞추려는 시도 (아직 매끄럽지 않음):
0. Importing MIDI makes project to start a new
1. Set project tempo .. but usually you don't know so
2. Start a new and import MIDI and some tempo will be usually set to something as indicated in the MIDI
3. Just use this value / You might want to think to remove the tempo of midi by going to tempo and right click to delete it but dont do this (no use)
4. Then import the audio (if you detect tempo (somewhere in left little icon)) ... use this function to set the tempo to project tempo
5. Still they are not exactly right
6. Two choices - stretch MIDI or stretch audio
7. Stretch MIDI is not only difficult (cannot do it all at once over different channels)
8. Even if you tried this, MIDI stretching is odd ...
9. So use audio stretch <-> icon somewhere in the left
10. But before stretching, align the beginning --> if you are lucky after alignment and whole stretch might work
11. But most likely tempo varies in the middle so you gotta chop at some milestones and stretch and paste togther piece by piece
13. Project tempo does not seem to matter

14. To slice and stretch audio individually, slice using knife, then stretch each by setting to <-> stretch mode and make sure you are in pencil, then you get different looking arrow cursor to stretch (not moving right and left)

> 매우 번거롭고 잘 안 됨. 남은 질문: bpm 삭제 방법, stretch 설정 방법, 마커/그리드에 정렬하는 법, 여러 구간을 다른 트랙에 복사·붙여넣기.

## 9. GM MIDI로 저장하기 ❓

- GM이 아닌 사운드를 쓴 MIDI를 저장할 때, 모든 사운드를 대응하는 GM 음색으로 바꿔야 하는가?
- 드럼은 **채널 10** 으로 설정.

## 10. 사운드 문제 해결 (Troubleshooting)

- FL Studio ASIO 문제일 수 있음 → 재설치가 필요할 수도 있다.
- FL Studio ASIO 와 USB 마이크는 같이 동작하지 않았다 (적어도 이 PC에서는).
- 오디오 카드에 연결한 non-USB 마이크는 잘 됨.
- ASIO4ALL + USB 마이크는 녹음은 되지만 소리가 안 남 → 실용성 없음.
- **Amon ASIO** (오디오 카드 사용) 가 소리 지연이 가장 적다. FL Studio ASIO는 약간 지연이 있다.

## 11. 학습 현황 (Learning Progress)

> 출처: `Manual2.pptx` (FL Studio 슬라이드)

| 주제 | 상태 |
| :--- | :--- |
| Channel rack 선택, 믹서 트랙 연결 (Ctrl+L / 메뉴), F8 플러그인 드래그 | ✅ 정리됨 (§2–3) |
| 복사 후 Ctrl+B로 옆에 붙여넣기 | ✅ 정리됨 (§3) |
| 기본 편집 및 편곡 (Basic editing & arrangement) | 🔄 진행 중 |
| MIDI 설정 | 🔄 진행 중 — [MIDI & Hardware Setup](MIDI-and-Hardware-Setup.md) |
| 오디오 인터페이스 | 🔄 진행 중 — §10 |
| Fake와 함께 연주하기 | ❓ |
| 녹음 / 스택 녹음 | 🔄 진행 중 — §4 |
| 여러 VST 이해 | 🔄 진행 중 |
| FL Studio 20 구입? | ❓ |
| FL Cheat Sheet | 📝 슬라이드 작성 예정 (현재 이 페이지가 대신함) |
