# MIDI & Hardware Setup

[← Home](README.md)

> 출처: `Manual2.pptx` (DAW / System set up, Connection 1·2), `Fake-setup-note-11-27.txt`, `FL-loop recording.txt`

---

## 1. MIDI 채널 (MIDI Channel)

대부분의 MIDI 메시지는 연결된 여러 장치 중 **하나의 장치**만 받도록 되어 있다. 채널은 장치를 구분하는 쉬운 방법이다. 예를 들어 채널 1용 메시지에는 채널 번호 1이 데이터에 들어 있고, 채널 1을 듣도록 설정된 장치만 반응한다.

> **원칙: 장치 하나 = 채널 하나 (one device, one channel)**

## 2. 학교 셋업 (Connection 1)

**구성**
- PC – USB 인터페이스 (RoMIO) – Yamaha
- 또는 PC – Yamaha 드라이버 – Yamaha (USB 직결)

**순서**
1. Yamaha 드라이버 다운로드·설치
2. MIDI 설정 (P70 매뉴얼): *Utility → MIDI → USB*
3. PC 쪽에서 MIDI in / MIDI out을 Yamaha로 지정
4. *Utility → Switch → Local Control* 설정
5. 악기를 GM 등으로 설정 (매뉴얼 참고). GM: *Multi/Seq → User → C 1*

**오디오 출력**
- Yamaha → AMP 입력 (CD) → 믹서
- 또는 PC → AMP 입력 (CD) → 믹서 (Yamaha 음원 대신 PC의 GM 음원을 쓸 때)

**Fakeplay 셋업 메모**
- Yamaha USB 직결 + Yamaha 드라이버는 잘 안 되는 것 같다 ❓
- RoMIO I/O는 동작하지만, 가끔 시스템이 멈춘다 ❓
- MIDI 출력이 동작하려면 MIDI 소스의 모든 트랙을 한 채널로 설정해야 한다 (반대로 모든 채널을 한 트랙으로? ❓)

> ❓ 매번 설정하지 않도록 이 설정을 저장하는 방법은?

## 3. 집 셋업 (Connection 2)

| 연결 | 내용 |
| :--- | :--- |
| PC – M-Audio – Korg | 아날로그 MIDI. 4x4 **out** → 키보드 **in**, 4x4 **in** → 키보드 **out** |
| PC – 오디오 인터페이스 | 마이크/오디오 입력 잭, 오디오 출력 → 스피커 |
| PC / 노트북 – AKAI | USB |

## 4. AKAI 멀티 악기 설정

- **AKAI SW editor** 로 채널을 1, 2번 등으로 따로 설정하고 RAM으로 보낸다.
- RAM이므로 전원을 껐다 켜면 다시 설정해야 한다.
- DAW 쪽 설정은 [FL Studio Guide → 루프 녹음](FL-Studio-Guide.md#4-녹음-recording) 참고.

## 5. PC MIDI Mapper

- **CoolSoft MIDI Mapper** 사용
- ❓ 매번 설치해야 하나? 가끔 이유 없이 매핑이 사라진다.

## 6. 오디오 인터페이스 & 스택 녹음

- Infrasonic / Amon 인터페이스는 Windows 10에서 동작하지 않음 → 새 오디오 인터페이스 구입 고려.
- Fakeplay를 녹음용 오디오 입력으로 쓰는 것도 고려.
- Jamstik은 MIDI 입력/출력으로 동작하지 않았다.
- ASIO 드라이버별 지연·호환성 메모는 [FL Studio Guide → 사운드 문제 해결](FL-Studio-Guide.md#10-사운드-문제-해결-troubleshooting) 참고.
