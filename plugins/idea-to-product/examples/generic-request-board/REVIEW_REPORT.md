# REVIEW_REPORT: 요청 관리 게시판

| 리뷰 유형 | 실행된 hook | 리뷰어 agent | 발견한 문제 | 위험도 | 추천 조치 | 사용자 확인 필요 여부 | 관련 문서 |
|---|---|---|---|---|---|---|---|
| 기능 추가 | feature-drift-gate.py | scope-guard, pm-reviewer | `실시간 채팅`은 MVP 요청 관리보다 커질 수 있음 | Yellow | v2 이동 권장 | Yes | DECISION_LOG.md |
| 와이어프레임 변경 | wireframe-change-review.py | product-flow-reviewer | 권한 없음 상태가 필요함 | Medium | permission-denied-state 추가 | No | wireframe.html, AC.md |
| 측정/기록 | measurement-coverage-review.py | measurement-reviewer | 상태 변경 기록 정책이 필요함 | Medium | POL-003, MEA-002 연결 | No | POLICY.md, MEASUREMENT.md |
| 최종 문장 | human-writing-final-pass.py | human-writing-editor | 금지 표현 없음 | Low | 유지 | No | 전체 문서 |
