# Readable Question Card

Question wording should be plain enough that the decision is clear at first read. Keep practical terms such as 권한정책, 상태값, 이벤트, 로그, PRD, AC, KPI, and `data-req-id` when they matter.

Use this structure:

```md
[질문 3/12]

화면 위치:
`wireframe.html`의 `data-req-id="request-submit-button"`

질문:
이 요청 등록 버튼은 누가 볼 수 있어야 하나요?

왜 묻나요:
권한정책을 정해야 개발자가 버튼 노출 조건을 구현할 수 있습니다.

선택지:

A. 로그인한 모든 사용자
- 장점:
- 주의:

B. 특정 역할을 가진 사용자만
- 장점:
- 주의:

C. 관리자가 허용한 사용자만
- 장점:
- 주의:

D. 잘 모르겠음
- 추천 기준:

내 추천:

추천 이유:

답변 방법:
A, B, C, D 중 하나를 골라도 되고, 직접 답을 써도 됩니다.
```

Flow question examples:

```md
진입과 다음 행동:
사용자는 어디서 이 화면으로 오고, 등록한 뒤 어디로 가야 하나요?

사용 규모:
이 요청 등록이 하루에 얼마나 많이 일어나길 바라나요?

품질 기준:
사용자가 많아져도 계속 괜찮게 쓰려면 어떤 규칙이 필요할까요?
```
