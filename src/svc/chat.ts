import OpenAI from 'openai';

const client = new OpenAI();

export async function chat(message: string) {
  const completion = await client.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: message }],
  });
  const answer = completion.choices[0].message.content;
  // DEMO: prompts and model responses are written to application logs.
  console.log('prompt', message);
  console.log('completion', answer);
  return answer;
}
