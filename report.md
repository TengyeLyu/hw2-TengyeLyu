# Report

## Business Use Case

The business use case is drafting customer support email responses for an online retail company. The system helps support agents reply to customer messages more efficiently while maintaining a consistent tone.

The user is a customer support agent. The input is a customer message, such as a complaint, question, or request. The output is a polite and professional draft email reply.


---

## Model Choice

I used the Gemini 3 Flash Preview model because it is fast and suitable for generating short text responses. I initially tried other models, but some were not available or caused errors. The selected model worked reliably for this task.


---

## Baseline vs Final Prompt Design

The initial prompt only asked the model to be polite and professional. However, the responses were sometimes too neutral and did not address customer emotions clearly.

In Revision 1, I added instructions about empathy and tone. This improved the quality of responses. The model became more supportive and better at handling frustrated customers.

In Revision 2, I added rules to prevent hallucination and risky behavior. For example, the model was instructed not to invent policies and not to promise refunds or compensation. This made the responses safer and more aligned with real business constraints.

Overall, prompt iteration improved both the tone and the reliability of the outputs.


---

## Failure Cases and Limitations

The system still has limitations. In some cases, the model may produce responses that sound correct but are not fully accurate. This is especially risky in situations involving refunds, compensation, or unclear policies.

The model may also avoid giving a direct answer and instead escalate too often, which could reduce efficiency. In high-risk cases, such as angry customers or policy-related questions, human review is still necessary.


---

## Deployment Recommendation

I would recommend partially deploying this system as a drafting assistant, not as a fully automated system.

The system can be used for low-risk and repetitive cases, such as password resets or delivery status questions. However, for complex or sensitive cases, a human agent should review the response before sending it.

This approach balances efficiency and safety. It allows the system to improve productivity while reducing the risk of incorrect or harmful responses.
