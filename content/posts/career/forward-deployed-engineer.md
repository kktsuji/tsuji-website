---
title: "An Engineer's Path in the Age of AI Coding — The Forward Deployed Engineer (FDE) Option"
description: ""
date: 2026-06-20T11:00:00+09:00
lastmod:
draft: false
---

## Summary

- With the spread of AI coding, **the work of writing code by hand has all but disappeared**. The center of gravity of an engineer's job has shifted from "implementation" to "**running the loop of drawing out customer requirements and validating them with an MVP**."
- **The Most Valuable Product (MVP—the minimal product that satisfies only the customer's most core requirement) is nothing more than a sounding board for raising the precision of requirements definition.** Building software is not the goal in itself.
- Customers are not aware of their own requirements. **Only by putting forward a hypothesis as a proposal and deliberately letting them reject it can hidden requirements be drawn out for the first time.**
- Designing the critical MVP that draws out requirements with minimal effort demands both **an engineer's experience and knowledge** and **the customer's domain knowledge**.
- Where these intersect is the **Forward Deployed Engineer (FDE)**. It can be one of the paths an engineer should pursue in the age of AI coding.

## Introduction

This article is a summary of the experience and the firsthand intuition I have gained on the front lines of AI-driven DX in manufacturing.

I work on AI-driven DX (digital transformation) at an image sensor company.

The biggest recent change in my work is that **the work of writing code by hand has all but disappeared**.

This does not mean I have moved away from development. Quite the opposite—my development output has increased. It is simply that, through the use of AI coding, the implementation step is no longer "work that a human spends time doing by hand."

So what does an engineer who no longer codes spend time on? And what kind of career comes into view beyond that?

In this article, starting from my own firsthand sense on the front lines, I argue the hypothesis that **one path an engineer should pursue in the age of AI coding is the Forward Deployed Engineer (FDE)**.

## AI Freed Engineers from the "Labor" of Coding

First, let me establish where we stand.

AI has ushered in **an era in which anyone can build software that more or less works**. Convey the requirements roughly, and AI writes the code in one go. A working prototype is in hand in tens of minutes—sometimes in minutes.

This change has fundamentally altered how engineers spend their working hours. In my case, the bulk of my current working time goes not to coding but to the following.

- Interviewing the staff of the business units that want to advance DX
- Understanding their operations and domain knowledge
- Proposal-based requirements definition grounded in that understanding

In other words, **the upstream time of discerning "what to build"** has come to occupy almost all of my work. Prototype (MVP) development itself is over in an instant thanks to AI.

What matters here is that **the fact that implementation got faster is not the essence**. The essence is that, because implementation got faster, **the source of an engineer's value has shifted to "the process of deciding what to build."**

## The MVP Is Not the Goal—It Is a Sounding Board for Drawing Out Requirements

There is something I have come to feel strongly through DX work: **the MVP is nothing more than a tool for raising the precision of requirements**.

This may sound a bit crude. But at least on my front lines, the MVP is not built to deliver value on its own; it is built as a **"sounding board" for drawing the true requirements out of the customer (the business unit)**.

Concretely, I run the following loop at high speed.

1. Conduct requirements interviews with the business unit
2. Form a hypothesis from what they say and propose a requirement: "Isn't this what you need?"
3. Develop an MVP based on that hypothesis
4. Show a demo and get feedback
5. Fine-tune the requirement based on the feedback
6. Rebuild the MVP based on the revised requirement
7. Repeat steps 2–6

One lap of this loop corresponds to a single sprint in agile development (roughly one to two weeks). Form a hypothesis, deliver something working in the form of an MVP, get feedback via a demo, and adjust the requirement in the next lap. In that it raises the resolution of the requirement little by little each sprint, it is exactly the same rhythm as agile's iteration.

The goal of this loop is not to build a finished product. It is to **raise the precision of requirements definition**. The MVP is merely a sounding board for that.

And with the advent of AI coding, **this loop can now be run at overwhelming speed**. Form a hypothesis, and within a few days you can build and show something that works. Get feedback, and you can rebuild it right away and put it up for the next demo.

This maps cleanly onto the **Build-Measure-Learn loop** long discussed in the startup world, and onto the idea that "an MVP is for maximizing validated learning about customers with the least effort." The goal of an MVP is not to build a product but to **learn**. AI has dramatically raised the rotation speed of that learning cycle.

## Customers Don't Know Their Own Requirements — Rejection Gives Birth to Requirements

Here I want to state what I consider most important about requirements interviewing.

It is the fact that **customers are not aware of their own requirements**.

Ask from a blank slate, "Please tell me your requirements (what you want to do or what's troubling you)," and usually nothing comes out. Even when something does, it tends to be superficial and off from the problem that truly needs solving. This is not the customer's fault. It is because **the human brain is far better at criticizing or fine-tuning something that already exists than at creating something from nothing**.

So our strategy becomes this:

First, we form a hypothesis and make a concrete proposal: **"Isn't this what you need?"**

Only then can the other party react. "No, that part is a little off." "This other thing is more important." **It is precisely within this rejection and correction that the true requirement—one the customer themselves had not noticed—lies hidden.**

And by showing that proposal **not merely in words but as a working MVP**, the resolution of their reaction rises further still. When there is something they can actually touch and see, people start to speak more concretely: "This is wrong." "I want this part to be like this." Only after building and showing an MVP based on the hypothesis do **requirements the customer themselves had not even noticed** finally emerge.

By the way, what is decisively important here is our **mindset**.

Both the proposed requirement and the MVP demo are **nothing more than sounding boards put forward on the premise of being rejected**. Therefore, there is no need to get angry or discouraged when rejected. Quite the opposite. When rejected, you should see it like this:

> Good—I've drawn out one more hidden requirement.

Rejection is not failure but progress. Whether you can hold this mindset is what separates being able to keep running the loop soundly and at high speed from not.

As an aside, the phenomenon of "deliberately throwing out a wrong answer to draw out the right one" is known in the internet world as Cunningham's Law: "The best way to get the right answer on the internet is not to ask a question; it's to post the wrong answer." People are far more strongly motivated to correct a mistake than to fill in a blank. What happens in requirements interviewing is essentially the same. The proposal and the MVP are high-quality "wrong answers" for drawing out the other party's "that's wrong."

## Where AI Coding Really Makes the Difference

Having read this far, you might think, "If anyone can build an MVP with AI, then in the end everyone can do the same thing."

It is true that anyone can now build "something that more or less works" with AI.

But **truly good software**—and above all, **designing the critical MVP that draws out requirements at the fastest speed and with the least effort**—is not something just anyone can do.

That is because it requires the following two things.

- **An engineer's experience and knowledge**: What is technically sound and what will break down. Where to build things out and where to cut corners so that, with the least effort, you precisely hit only the hypothesis you want to validate. This feel for design can only come from an engineer's accumulated experience.
- **The customer's domain knowledge**: What should be validated in the first place, which hypotheses are essential, and which feedback is a genuine signal. Seeing through this requires a deep understanding of the customer's operations and domain.

AI takes over implementation. But **the power to answer the very question of "what hypothesis should be validated next, with what MVP"** still lies on the human side. And that power is precisely what makes the greatest difference, and is hardest to replace, in the AI era.

Put another way, just as AI has commoditized the labor of coding, **the scarcity of "an engineer's design ability × the customer's domain understanding" has relatively skyrocketed**.

This change is easier to grasp through the contrast of "How" versus "What and Why." Translating into technical specifications, and the coding that implements them—the **"how to build it" (How) is rapidly being replaced by AI**. On the other hand, **the power to draw out customer requirements, form hypotheses and propose them, and—grounded in domain understanding—discern "what to build" (What) and "why to build it" (Why)** still remains on the human side. And an engineer's value going forward will be determined precisely by whether they can take hold of this What and Why. The question is not whether you keep honing How, but **whether you can shift your center of gravity toward What and Why**.

## That Is Why the FDE Matters

To sum up the discussion so far in one line:

**In the era ahead, talent that combines an engineer's design ability with the power to dive deep into the customer's domain will be decisively important.**

And the very role that points to this image is the **Forward Deployed Engineer (FDE)**, which has been drawing worldwide attention in recent years.

The FDE is a role said to have originated at Palantir, referring to **an engineer who dives deep into the customer's front lines and handles everything end to end—from understanding requirements through design, implementation, integration, and deployment**. They embed in the customer's team, understand the operations, and themselves build and deliver what truly works.

This role has rapidly grown in prominence in the AI era. The prominent venture capital firm a16z has called the FDE "the hottest job in startups." In fact, it has been reported that monthly job postings for FDEs increased by **more than 800%** from January to September 2025. AI companies, OpenAI among them, are actively hiring not just engineers who build models but **engineers who actually make those models work on the customer's front lines**.

Why does the FDE work? It becomes visible when contrasted with existing roles.

- **Consultant**: Strong on upstream problem framing and strategy. But **lacking an engineer's perspective**, they have no means to validate by getting their own hands dirty. Their proposals tend to stop at "pie in the sky."
- **Contract development**: Strong on the downstream of giving shape to a given specification. But they **do not step into upstream requirements definition**. And this very "implement exactly as specified" step is also the part most easily replaced by AI.
- **FDE**: Handles everything from upstream requirements definition to downstream implementation and deployment, **end to end and grounded in domain understanding**. They connect a consultant's upstream strength and an engineer's implementation strength within a single person.

In other words, the FDE takes "the best of both" consulting and contract development while fitting perfectly into the role that delivers the most value in the AI era: "running the loop of drawing out requirements at high speed."

And here is what I most want to convey.

**If a person who has built a career as an engineer can acquire a consultant-like perspective and ability—that is, the power to dive into the customer's domain and draw out requirements—in other words, if they can become an FDE, there is a chance they become an extremely powerful and scarce talent.**

For an engineer, acquiring a consultant-like perspective after the fact is by no means impossible. Rather, precisely because AI has now freed us from the labor of coding, we can invest that time in "customer understanding" and "the craft of drawing out requirements." An engineer who already has the foundational technical ability could be said to stand at the shortest distance to becoming an FDE.

## Closing

With the advent of AI coding, the scarcity of merely "being able to write code" will surely decline. If all you need is to build something that works, anyone can already do it.

What will matter instead is the multiplication of **"the power to draw out requirements × domain understanding × engineering."** Drawing out requirements the customer themselves had not noticed, using the sounding board of hypotheses and MVPs; polishing them through a high-speed validation loop; and designing and delivering what truly works. This whole sequence of moves is, I believe, the greatest value a human engineer can provide in the AI era.

And standing right where that multiplication intersects is the Forward Deployed Engineer.

Of course, I do not intend to claim that the FDE is the one and only right answer for every engineer. But I am certain it is **one of the leading options an engineer should consider in the age of AI coding**. At the very least, my own firsthand sense on the front lines points straight in this direction.

If you are lost about your own career in the AI era, first try running this loop on a small scale on your own front lines. Form a hypothesis, show it as an MVP, get rejected, and rebuild again. Within that repetition, a new place to stand as an engineer will surely come into view.

## References

- [Forward Deployed Engineer — Wikipedia](https://en.wikipedia.org/wiki/Forward_Deployed_Engineer)
- [a16z, "Trading Margin for Moat: Why the Forward Deployed Engineer Is the Hottest Job in Startups"](https://a16z.com/services-led-growth/)
- [The Pragmatic Engineer (Gergely Orosz), "What are Forward Deployed Engineers, and why are they so in demand?"](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers)
- [Palantir Blog, "A Day in the Life of a Palantir Forward Deployed Software Engineer"](https://blog.palantir.com/a-day-in-the-life-of-a-palantir-forward-deployed-software-engineer-45ef2de257b1)
- [PYMNTS, "Forward-Deployed Engineers Emerge as One of AI's Fastest-Growing Jobs"](https://www.pymnts.com/artificial-intelligence-2/2026/forward-deployed-engineers-emerge-as-one-of-ais-fastest-growing-jobs/)
- [Eric Ries, _The Lean Startup_ / Lean Startup Co., "What Is an MVP?" (Build-Measure-Learn; MVP = validated learning)](https://leanstartup.co/resources/articles/what-is-an-mvp/)
- [Cunningham's Law — Meta-Wiki](https://meta.wikimedia.org/wiki/Cunningham%27s_Law)
- [Requirements elicitation — Wikipedia (requirements elicitation via prototyping)](https://en.wikipedia.org/wiki/Requirements_elicitation)
