# FakeBass Project

[← Home](README.md)

> 출처: `가칭 FakeBass 가상환경 디자인 및 인터액션 안2.pptx`, `fakebass13.txt`, `fakebass.txt`, `Manual2.pptx` (Music Programming)

**FakeBass** (가칭)는 가상환경에서 뮤직비디오를 보면서, 미디 컨트롤러 등으로 **베이스 리듬을 쉽게 연주**하는 인터랙션 디자인안입니다.

---

## 1. 개념 (Concept)

- 가상 공간 안의 가상 화면에 **뮤직비디오**를 띄운다.
- 헤드셋으로 몰입형으로 보며 인터랙션한다 (360도 비디오면 더 좋다).
- 사용자는 미디 컨트롤러나 다른 디바이스로 **리듬 등을 입력**한다.
- 화면 위에 필요한 정보를 시각화한다.

## 2. 리듬 선택 & 시각화

리듬 소스:
- 4/4박 표준 리듬 패턴 여러 개
- 또는 해당 곡에서 미리 추출한 **Signature Bass Riff** 몇 개
- 또는 MIDI 사전 분석으로 악보 그대로

시각화 (리듬 게임 방식):
- 노트가 왼쪽의 빨간 **finish line** 으로 흘러간다.
- "지금 곧 연주될 리듬"과 "다음 리듬"을 보여주고, 어떤 리듬을 할지 선택할 수 있다.
- 손을 쓰기 어려우므로 선택은 **Gaze** 또는 non-dominant hand 커서, 들고 있는 디바이스 끝으로 조준 등으로.
- 선택하지 않으면 기본 리듬 또는 이전 리듬을 계속한다.

## 3. 인터랙션으로 MIDI 소리 만들기

- 리듬의 음은 코드에 맞춰 MIDI로 연주한다 (예: C 코드면 근음 C).
- 리듬의 계음은 사전 MIDI 분석이나 수동으로 캡처.

### 연주 모드 (난이도)

| 모드 | 사용자 입력 | 나머지 |
| :--- | :--- | :--- |
| **Automatic** (쉬움) | 첫 박에만 입력 (키보드, 터치 등) | 선택된 리듬/코드가 자동 연주 |
| **Play gesture** | 첫 박 즈음 짧은 "리듬 제스처" — 리듬마다 고유 제스처, 미리 선택 안 함 | 인식되면 나머지 자동 연주 |
| **Semi-automatic** | 4분음표 박 중 1·2, 1·3, 1·2·3·4, 1·4 등만 타이밍 맞춰 입력 | 실제 리듬은 자동 연주 |
| **Manual** (어려움) | 모든 리듬 음표를 time window 안에서 finish line에 맞춰 입력 | tolerance로 난이도 조정. 제스처/타이밍이 안 맞으면 연주 정지 |

- Play gesture 모드에서는 인식 지연이 문제가 될 수 있다 → 첫 박은 무조건 자동으로 하는 옵션, 반 마디는 자동 연주 + 제스처 인식, 나머지 반 마디만 제스처로 변화.

### 추가 아이디어
- **Random variation 모드**: 선택된 리듬에 가끔 무작위 변화를 준다.
- 시각 효과: 리듬 게임처럼 맞출 때 터지는 효과.
- 노트/타이밍 입력뿐 아니라 **액션**도: 영상·음원에서 동기화된 이벤트를 분석해 액션 이벤트로 (예: 기타 뱅).
- 코드 체인지 때 non-dominant hand가 무언가를 (기타 왼손처럼) — difficult 모드?
- ❓ 코드 라벨이 붙은 MIDI 패드와 무엇이 다른가?

참고: [Jammy E (playjammy.com)](https://playjammy.com/jammy-e/), [YouTube 데모](https://www.youtube.com/watch?v=k8mnntmhD-M) — 미디 기타 하나 주문함.

## 4. 베이스 인터페이스 디자인

- 실제로 기타처럼: **왼손으로 음을 선택**하고, **오른손으로 세팅된 줄들로 리듬**을 탄다.
- 흘러가는 리듬 게임 터치 인터페이스 (R ↔ L): 마디/몇 마디 단위로 L→R, L→R. 화면과 손이 반대 방향으로 흐르며 베이스 라인을 일부 그린다.
  - 예: `1-1-3 : 5 1 : 사이:1 사이:1 사이:1 사이:3, …`
- 화면과 손의 싱크가 관건 → 낮은 threshold로 해결?
- AI 또는 사전 지식으로 음악 **context** (코드, 템포) 인식 → 코드에 따라 모든/지정 키가 고정된다.
  - 버튼: **1st, 3rd, 5th, 6th, 7th** (chord tone) + **사이음** (non-chord tone)
  - Triad, 7th, 6th, minor
- 손가락 터치뿐 아니라 튕기기, 손가락 움직임에 의한 모듈레이션, 손에 들고 뱅잉도 가능할 듯.
- AI로 무작위 리듬이나 음 추가.

### 코드 연주로 확장
- 왼쪽에 **Inversion** 버튼
- 표기: `/` 동시, `,` 다음, `:` 마디 구분
  - 예: `1-3-5 / 7 : 1-3-5 : 1-3-5/6, 사이음, 1-3-5 : 1-3-5, 사이음, 1-3-5/6`
- 왼손으로 선택, 오른손은 여러 손가락 동시 누르기 또는 아르페지오. 손이 굳이 오른쪽으로 갈 필요 없음.

## 5. 시스템 아키텍처 (Plan)

```
 Keyboard / Device (I1, I2)
            │
            ▼
   ┌──────────────────┐
   │      Unity       │ ← Rhythm game import
   │                  │ ← MP4 streaming
   └──────────────────┘
            │
            ▼
   Synchronization: MIDI / MP3 / MP4
   (Filter / Optimization, HMM accompaniment)
```

---

## 6. 리서치 키워드 (`fakebass13.txt`)

- **Music Interaction**, **Multitasking**
- **Non-physical → Observation**: 제스처, 표정, 전신, 세부 국소 동작, 악보
- **Physical → Instrument**
- 운전·비행·스포츠에도 적용 가능?

**AI와 시각화가 경험을 어떻게 개선할 수 있나**
- AI — 기술(skill) 문제
  - 여전히 여러 곳에 집중해야 함. 빠르게 진행될 때 맥락을 잃지 않으려면?
  - **어디를 볼지 안내** (사용자가 모를 수 있으므로) vs. 전문가에게는 맡김
  - 큰 그림으로 주의를 유도하되, 때로는 작은 그림도
  - 정보 (악보)와 관련 동작/표현/이벤트 연결 → 미리 분석, 실시간 추출
- 시각화
  - AR, Head-up display
  - 자유롭게 움직이는 HUD를 관련 이벤트가 일어나는 고정 위치에 정렬할 수 있나? HUD가 기타와 함께 움직이나?
- 운전·스포츠·오케스트라 연주에도 적용?
  - 두 운전자가 한 통로를 지나가는 상황?
  - 목표 lock-on? threshold 안에서?
- Variation → 어떻게 변화를 줄까?
- \* no-look pass는 왜 특별한가?

## 7. Music Programming 할 일 (`Manual2.pptx`)

- Fake 프로그래밍 개선, 재구현?
- Expression control
- Python export, Phone export
- FakeBass 프로젝트
- MP3 기반 Fake

실험 코드는 [Python for Music](Python-for-Music.md) 및 [`code/fakebass_sketches.py`](code/fakebass_sketches.py) 참고.
