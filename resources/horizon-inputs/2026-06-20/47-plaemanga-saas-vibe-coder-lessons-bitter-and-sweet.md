# Input 47 — Plaemanga: 8 bitter lessons + 3 sweet lessons of building SaaS with AI vibe-coding

**Source:** Long-form Thai-language post by the author of **Plaemanga** (a manga-translation SaaS built with AI vibe-coding). The post explicitly notes *"Human เขียนเอง 100% นะครับ"* — human-written, not AI-generated. This matters: it's a first-person practitioner account, not aggregator content.

The post is structured as **bitter lessons** (what failed) followed by **sweet lessons** (what worked). It is the **most honest practitioner-perspective input** in today's brief — and one of the few that doesn't fit the "promote and sell" pattern most Thai-language educational content follows.

## The 8 bitter lessons (paraphrased)

1. **Assuming this thing is useful enough that someone will pay** → ship features you love that nobody uses. **What to do:** talk to people who *actually have the problem* AND are *desperate enough to pay.* Distinguish *"this is great"* (polite) from *"I will buy this"* (real).
2. **No one uses your SaaS** → keep adding features / re-skinning / moving buttons. **What to do:** the failure is either (a) bad marketing or (b) product doesn't actually solve the problem. Ask the people who saw your promotion and scrolled past — *why?* Often the product *does* solve their problem but your communication didn't make it clear.
3. **Building something you don't care about (you started for the money)** → all you think about is annual plans / subscription system / payment gateway *before* you've written code. **What to do:** build from a real pain you have or are deeply curious about. Save subscription/payment work for when someone actually asks *"how do I pay you?"* Don't burn 2 weeks on Stripe for an app with no users.
4. **Over-provisioning hosting on day 1** → host costs more than AI + electricity combined when you have <10 monthly users. **What to do:** start free or near-free (Cloudflare Pages + cheap backend that can scale). For most webapps, the *traffic-overwhelms-you-on-day-1* scenario almost never happens unless you're a startup spending heavily on launch marketing.
5. **Marketing = paying for ads** → expecting ads to bring users *proportional* to spend. **What to do:** ads are MSG — they amplify a product that's already working, they don't carry a product that isn't. What helps new SaaS most: **organic content** (e.g., articles that teach + softly sell — *like this post you're reading*), or community-targeted sharing in the right communities.
6. **Listening to everyone's feedback** → trying to fix everything for everyone → impossible. **What to do:** weight feedback by *target audience* AND by *people who pay or use repeatedly.* Distinguish *loud voice* from *important voice.*
7. **Tech stack chosen for tech stack** → architecture decisions for an app with no users. **What to do:** use what ships fastest, cheapest, with your strongest fingers. Last week's hyped framework is rarely the right choice. The best stack for your product is often *the least complex one that does the job.*
8. **Celebrating vanity numbers** → 500 signups, 3 active, declaring victory. The numbers that matter: *repeat-use* + *paid.* The vanity number can mean *marketing works but product doesn't.*

## The 3 sweet lessons (from his Plaemanga experience)

1. **Costs near zero** — he runs home-lab infrastructure (servers + GPU cluster) + solar off-grid → no real risk of running at $0 revenue for a year. Only domain cost. Lets him survive while learning.
2. **Was a user first (manga translator)** — built the tool for himself. *"I am the Product Owner, the User, and I know the whole process from input to output."* Solves real pain because the pain is his.
3. **Still uses it daily + develops alongside** — being the product's own user keeps it solving actual problems, not imagined ones.

## The author's own framing of the meta-test

> *"If you yourself wouldn't pay for it, why would anyone else?"*

That sentence is the *MVP-validation-test* in one line.

## Why this matters for Horizon — the practitioner-honest counterweight

Across today's 46 prior inputs, much of the content has been **aggregator-curated** (lists of tools, infographics summarizing principles). Input 47 is **practitioner-written** — someone who actually shipped a SaaS using vibe-coding, failed in identifiable ways, learned, and shared honestly without hard-selling at the end. **It is the rarest format in the Thai-language AI-education community: practitioner failure-and-success without a course pitch.**

Horizon's curriculum should:

1. **Lift the 8-bitter-lessons + 3-sweet-lessons format as a teaching pattern** — it's the most digestible practitioner-confession shape, immediately applicable for any Horizon learner shipping their first SaaS.
2. **Embed this post (with permission) as a Horizon Research case study** — *the practitioner-honest counterweight* to the aggregator content the brief catalogues elsewhere.
3. **Use the *"if you wouldn't pay, why would anyone"* test as M3's most concrete diagnostic** — pairs with the Invisibility Test (Input 25) and the Skill Preservation principle (Input 26).

## Three Horizon placements

**M3 diagnostic addition** — *"The pay-it-yourself test."* Goes in alongside the tier-ladder self-diagnostic from Input 14.

**M4 capstone integration** — the 8 bitter lessons become the *"what you'll fail at first"* preview of M4's real-systems lesson, helping learners pre-empt the canonical failure modes.

**Horizon Research paper #19 seed** — ***"What Practitioners Actually Learn Building SaaS with AI: A Thai-Language Field Report (Plaemanga Case Study)."*** Direct embedding of this post (with permission) + Horizon's annotations connecting each lesson to the curriculum module that teaches it.

## Cross-references

- **[[Input 41 — Acemoglu]]** — practitioner-level confirmation of Acemoglu's macro-skepticism: AI doesn't make SaaS-shipping easy; it makes shipping faster but not paying-customer-getting easier
- **[[Input 25 — Bland AI / Invisibility Test]]** — Plaemanga's *"I am my own user, the product solves my real pain"* is the same insight as the Invisibility Test from the user perspective: success is invisible because the user (you) just keeps using
- **[[Input 28 — Prototype-first vs Plan-first]]** — Plaemanga is a textbook prototype-first build that worked because the prototype solved a real personal pain
- **[[feedback-always-mvp-make-it-exist-first]]** — Non's own MVP principle is exactly what Plaemanga's author lived through

Source: Thai-language LinkedIn-style post about Plaemanga (manga-translation SaaS); author self-identifies as a former manga translator.
