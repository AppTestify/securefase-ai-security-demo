import OpenAI from 'openai';

const client = new OpenAI();

// DEMO: untrusted request fields are interpolated into the system prompt.
app.post('/summarise', async (req, res) => {
  const { text, tone } = req.body;
  const completion = await client.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      { role: 'system', content: `You are a summariser. Write in a ${tone} tone.` },
      { role: 'user', content: text },
    ],
  });
  res.json(completion.choices[0].message);
});
