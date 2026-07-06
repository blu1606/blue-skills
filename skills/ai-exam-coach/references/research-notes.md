# Research Notes

Research conducted: 2026-07-06.

## Findings Applied

- Agent skills should use progressive disclosure: keep `SKILL.md` as an overview and load detailed references only when needed. Source: Anthropic skill authoring best practices, https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Strong MCQs require a clear stem, one correct answer for single-answer items, plausible distractors, and parallel options. Source: NC State DELTA, https://teaching-resources.delta.ncsu.edu/multiplechoice/
- MCQs and fill-in-blank are efficient for broad recall/understanding, but higher-order thinking needs scenario, essay, or rubric-based items. Source: University of Michigan CRLT, https://crlt.umich.edu/P8_0
- AI-generated MCQs improve when prompts include learning objectives, item-writing rules, source context, and explicit output format. Source: University of Michigan Online Teaching, https://onlineteaching.umich.edu/articles/generative-ai-for-course-design-writing-effective-prompts-for-multiple-choice-question-development/
- Knowledge bases for AI/RAG should be tested against representative questions, then repaired with clearer definitions, headings, summaries, and reduced ambiguity. Source: IBM watsonx docs, https://www.ibm.com/docs/en/watsonx/saas?topic=generation-optimizing-your-rag-knowledge-base

## Design Decisions

- Default to 20 questions because it is large enough for section coverage but small enough to avoid low-quality bulk generation.
- Split Common and track-specific topics to mirror the target exam style.
- Include MCQ, multi-select, fill-in-blank, scenario debug, and code because the target format mixes factual recall, applied judgment, and implementation.
- Always update KB after generation and grading so future exams adapt to learner state.
- Keep hidden context paths out of all generated artifacts.
