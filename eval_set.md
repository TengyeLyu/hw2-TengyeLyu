# Evaluation Set

This evaluation set is designed for the task of drafting customer support email responses.
It includes normal cases, edge cases, and higher-risk cases that may require human review.

## Test Case 1: Normal case
### Customer input:
Hi, my order has not arrived yet. Can you tell me where it is?

### What a good output should do: 
The reply should be polite, acknowledge the issue, and explain the next step clearly without sounding robotic.

## Test Case 2: Normal case
### Customer input: 
Hello, I forgot my password and cannot log into my account. Can you help me reset it?

### What a good output should do:
The reply should be clear and helpful, explain the reset process simply, and maintain a professional tone.

## Test Case 3: Edge case
### Customer input: 
I returned my item two weeks ago but I still have not received my refund. I am very disappointed.

### What a good output should do:  
The reply should show empathy, stay calm, and provide a reasonable next step without making promises it cannot confirm.

## Test Case 4: Likely failure or human review case
### Customer input: 
Your company is awful. I want a full refund, extra compensation, and I want you to guarantee this will never happen again.

### What a good output should do:  
The reply should remain polite and professional, avoid matching the hostile tone, avoid making unauthorized promises, and suggest escalation to a human agent if needed.

## Test Case 5: Policy ambiguity case
### Customer input:  
Can I return an item after three months if I already opened it?

### What a good output should do:  
The reply should not invent a return policy. If the policy is unknown, it should say that the case needs review or refer the customer to the correct support channel.