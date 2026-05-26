# AC: 요청 관리 게시판

| ID | 관련 요구사항 | 우선순위 | 운영 의도 | 확장 가능성 | 관련 화면 data-req-id | 관련 정책 ID | 관련 측정/기록 ID | Given | When | Then | 비고 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AC-001 | 요청 등록 | Must-have | Pilot | 확장 가능 | request-submit-button | POL-001 | MEA-001 | 로그인한 사용자가 요청 제목과 내용을 입력했다 | 요청 등록 버튼을 누른다 | 새 요청이 `접수` 상태로 생성된다 | 제목과 내용은 필수 |
| AC-002 | 요청 목록 확인 | Must-have | Pilot | 확장 가능 | request-list-section | POL-001 |  | 요청이 1개 이상 존재한다 | 담당자가 목록 화면을 연다 | 요청 제목, 상태, 등록일이 표시된다 |  |
| AC-003 | 빈 상태 표시 | Must-have | Pilot | 확장 가능 | empty-request-state |  |  | 등록된 요청이 없다 | 사용자가 목록 화면을 연다 | 빈 상태 안내가 표시된다 |  |
| AC-004 | 상태 필터 | Must-have | Pilot | 확장 가능 | request-status-filter |  |  | 요청 목록에 여러 상태가 있다 | 담당자가 `완료` 상태를 선택한다 | `완료` 상태 요청만 표시된다 |  |
| AC-005 | 상태 변경 | Must-have | Pilot | 확장 가능 | request-status-change | POL-002 | MEA-002 | 담당자가 요청 상세를 보고 있다 | 상태를 `완료`로 변경한다 | 요청 상태가 `완료`로 저장되고 변경 기록이 남는다 | 기록 정책은 POL-003 참고 |
| AC-006 | 상태 변경 | Must-have | Pilot | 확장 가능 | permission-denied-state | POL-002 |  | 담당자가 아닌 사용자가 상태 변경을 시도한다 | 상태 변경 버튼을 누른다 | 권한 없음 안내가 표시되고 상태는 바뀌지 않는다 | 권한 없음 상태 |
