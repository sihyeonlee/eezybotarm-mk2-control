# eezybotarm-mk2-control

## About
해당 Repository는 오픈 모델인 eezybotarm mk2를 제어하는 소프트웨어 개발을 목적으로 합니다.

## System Info
### NodeMCU
 - Micro Python
### PC
 - Python 3.7

## Log
- 2019-04-07 ~ 2019-04-09 eezybotarm mk2 프린팅 부품 출력
- 2019-04-10 ~ 2019-04-11 eezybotarm mk2 부품 조립 및 수동 작동 테스트
- 2019-04-12 NodeMCU 이용한 회로 설계 및 조립
- 2019-04-13 서보모터 불량 확인 (부품 재수급까지 잠정 중단)
- 2019-04-18 부품 재수급 및 작동 확인 테스트
- 2019-04-19 NodeMCU에 Micro Python 작동 확인
- 2019-04-20 NodeMCU 불량으로 부품 재수급 및 회로 재설계
- 2019-04-21 게임패드를 이용하여 eezybotarm 컨트롤
- 2019-04-23 UART 통신으로 게임패드와 eezybotarm 연동
- 2019-04-24 코드 간결화
- 2019-04-25 Micropython에 MQTT 적용 방법 고안
- 2019-04-26 Micropython MQTT 오픈 소스 사용 시도
- 2019-04-27 MQTT 소스 수정 실패 및 UDP 프로토콜 규칙 설계
- 2019-04-28 1차 시도 -> 극심한 딜레이 문제로 수정 필요
- 2019-04-29 딜레이 문제 수정 중... -> TDT 프로젝트 매우 심각한 오류 발생으로 해당 프로젝트 임시 보류. 예상 복귀일 5월 3일
- 2019-05-03 USB Controller 연결 확인에서 value 오류 확인하여 수정
- 2019-05-04 기존 UDP 방식 소스 코드 폐기 및 재설계
- 2019-05-05 UDP 통신 방식 프로그램 계속 진행
- 2019-05-06 기존 소스코드 스타일 수정 및 NodeMCU의 UDP 코드 작성
- 2019-05-07 UDP 통신 방법으로 Bot Arm 제어 확인