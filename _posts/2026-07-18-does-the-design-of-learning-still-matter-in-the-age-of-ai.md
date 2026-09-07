---
title: "Does the Design of Learning Still Matter in the Age of AI?"
description: "Three studies on AI and learning, and why the design decisions behind an AI tutor are what make the difference."
tags: [AI]
---

If you ask ChatGPT to explain the quadratic formula, photosynthesis process, or why World War II started, you will receive an answer in seconds. You can also ask for a simple explanation, a worked example, or another way to explain it. Better still, your AI friend has endless patience and will respond even at 3am. It is a little dazzling! And if you design learning for a living, as I do, you may start to wonder: If AI can explain anything to anyone, does the design of learning still matter?

Researchers have asked similar questions in the past. In 1983, Richard Clark reviewed decades of studies that compared one teaching medium with another and wrote one of the most widely quoted sentences in the field. Media are “mere vehicles that deliver instruction but do not influence student achievement any more than the truck that delivers our groceries causes changes in our nutrition” (Clark, 1983, p. 445). When performance improved after a new medium was introduced, Clark usually attributed the gain to the instructional method that came with it, or to novelty, not to the medium itself.

So, is AI just another truck? I think there is another question to ask this time: **Will the truck change the types of groceries delivered?** Clark’s vehicles delivered instruction without altering it. Generative AI, however, can change what learners receive each time learners ask a question, write a prompt, or share something about themselves.

## What does AI-assisted learning entail?

Bastani et al. (2025) provide some of the answers. In fall 2023, they conducted a preregistered field experiment with nearly 1,000 students in grades 9 through 11 across about 50 mathematics classes at one Turkish high school. All students received the same teacher-led instruction first. The researchers then assigned the classes to three conditions for the practice session.

One group used **GPT Base**, a chat interface similar to ChatGPT. Its prompt asked GPT-4 to act as a tutor and help the student solve the problem. Another group used **GPT Tutor**. It had the same interface, but its prompt included a set of safeguards such as teacher-written solutions, common student mistakes, and hints. The prompt also instructed the model not to give away the full solution. Students in the **control group** used only their notes and textbook.

After practice, everyone took a closed-book exam without AI. Each exam problem tested the same concept as a problem the students had just practiced.

During practice, students assigned to GPT Base scored 48% higher than students in the control group. Students assigned to GPT Tutor scored 127% higher than students in the control group. Those numbers make both tools look promising, right?

But here is the twist.

On the unassisted exam, students who had practiced with GPT Base scored 17% lower than students in the control group. Students who had practiced with GPT Tutor did not score significantly differently from the control group. So, the safeguards prevented the decline seen with students using GPT Base, but students using GPT Tutor did not do better than students using notes and a textbook.

## What went wrong?

The researchers then considered two explanations for the lower GPT Base exam scores. First, GPT-4 might have given students incorrect answers. When the researchers repeatedly asked GPT Base for answers to the 57 practice problems, it returned a correct answer in 51% of trials. Its logical errors predicted lower scores on assisted practice problems, but the researchers found no statistically significant spillover to the paired exam problems. So, incorrect answers may not explain the lower exam performance.

Second, students might have used it as a crutch instead of engaging with the mathematics. The researchers classified two types of messages: superficial message which repeated the problem or asked for an answer and nonsuperficial message which attempted an answer or asked for help. For students working with GPT Base, superficial first messages rose from 56% to 67% across the session. In the GPT Tutor condition, they fell from 42% to 37%. It is clear that the two designs elicited different ways of interacting with the AI.

Fan et al. (2025) found a related pattern in a study on teaching university writing with AI. They asked 117 Chinese university students who used English as a second language to revise an essay. The researchers randomly assigned students to four conditions: ChatGPT, a human expert, checklist tools, or no additional support. They restricted ChatGPT to giving advice rather than generating the essay, although they observed some students copying example sentences that it supplied!

Students in the ChatGPT group improved their essay scores by 3.60 points on average. The mean improvements were 1.63 points in the no-support group, 1.48 in the human-expert group, and 1.40 in the checklist group. The improvement in the ChatGPT group was significantly greater than the improvement in each of the other three groups.

However, the ChatGPT group’s advantage in essay revision did not extend to other measures. The four groups did not differ significantly in knowledge gain, on a transfer test about a related topic, or on any post-task motivation dimension: interest and enjoyment, perceived competence, effort and importance, or pressure and tension.

And here is the most interesting finding. During revision, students in the ChatGPT group repeatedly moved between writing and ChatGPT. Students working with the human expert did not form that loop with their expert. Their revising stayed tied to the reading materials, and they kept moving between the task instructions and their own checking of the draft. The authors read the pattern shown by the students using ChatGPT as potential *metacognitive laziness*. That is, students offloaded some of the work of regulating their learning to AI.[^1]

[^1]: The term describes an inference from trace patterns, not a disposition that the researchers measured directly.

## What can we design differently?

Please do not get me wrong. We do have evidence showing that AI can improve learning measured after the lesson, not just performance during it.

Kestin et al. (2025), for example, developed a GPT-4 tutor around research-based instructional practices. The tutor prompted active engagement, managed cognitive load, promoted a growth mindset, guided students through each problem in sequence, and used instructor-written step-by-step solutions.

The researchers then conducted a crossover experiment with 194 students in an introductory physics course at Harvard during fall 2023. Each student completed one lesson with the AI tutor at home and another through in-class active learning. The median posttest score was 4.5 after the AI-tutored lesson and 3.5 after the active-learning lesson, against a combined pretest median of 2.75. Students spent a median of 49 minutes with the tutor, compared with 60 minutes allocated to learning in class. They also reported feeling more engaged in the AI condition.

The authors set clear limits around this result. They write that they “do not presume that structured AI tutoring will always outperform in-class active learning in all contexts, for example, those requiring complex synthesis of multiple concepts and higher-order critical thinking” (Kestin et al., 2025, p. 6). They also argue that AI tutors should not replace in-person teaching.

Taken together, these studies do not tell a simple story about AI. GPT Base offered help without safeguards and was associated with lower unassisted exam scores than the control condition. GPT Tutor offered hints, withheld answers, and produced no significant difference from the control condition on the exam. Kestin’s tutor paired instructor-written step-by-step solutions with a platform developed over months to structure students’ progress. The same students learned more from the AI-tutored lesson than from the in-class lesson.

Three studies cannot settle the question. The participants ranged from ninth graders at one Turkish high school to undergraduates at Harvard. The AI was used to support practice after a lesson, help students revise an essay, or deliver the lesson itself. The comparison conditions also differed. We cannot attribute the different results to one design feature alone.

However, one pattern is clear. Someone has to decide what an AI tutor will provide and/or hold back, when it will offer a hint, how it will sequence a problem, and which mistakes it will anticipate. Each choice is a learning design decision. Each depends on an understanding of how people learn. **The design is what makes the difference.**

That said, our work may change a bit when we design learning with AI. Designing the prompts and structures that guide how AI interacts with students is becoming part of what we do. The work can be challenging because we need to understand **AI’s instincts**. A teacher who improvises in the moment draws on years of teaching and years of being a learner. Those instincts are usually worth following. An AI has instincts too (and this is where the truck may change the groceries): Because AI is trained to be helpful and fluent, it may “happily” hand over an answer to students when learning requires a hint, a question, or time to struggle. Learning designers must know how to guide AI to support learning. Doing this well requires a good understanding of how AI works as well as how learning works.

## References

Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences, 122*(26), Article e2422633122. <https://doi.org/10.1073/pnas.2422633122>

Clark, R. E. (1983). Reconsidering research on learning from media. *Review of Educational Research, 53*(4), 445–459.

Fan, Y., Tang, L., Le, H., Shen, K., Tan, S., Zhao, Y., Shen, Y., Li, X., & Gašević, D. (2025). Beware of metacognitive laziness: Effects of generative artificial intelligence on learning motivation, processes, and performance. *British Journal of Educational Technology, 56*(2), 489–530. <https://doi.org/10.1111/bjet.13544>

Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI tutoring outperforms in-class active learning: An RCT introducing a novel research-based design in an authentic educational setting. *Scientific Reports, 15*, Article 17458. <https://doi.org/10.1038/s41598-025-97652-6>
