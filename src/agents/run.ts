import OpenAI from 'openai';
import { exec } from 'child_process';

const client = new OpenAI();

export async function solve(task: string) {
  const completion = await client.chat.completions.create({
    model: 'gpt-4o',
    messages: [{ role: 'user', content: task }],
  });
  const command = completion.choices[0].message.content;
  exec(command);
  return eval(command);
}
