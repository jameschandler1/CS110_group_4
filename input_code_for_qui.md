# Simple multiple-choice quiz for "Weapons of Math Destruction"

questions = [
    "Q0. In the Introduction, O’Neil argues that “Weapons of Math Destruction” (WMDs) share three key traits. "
    "Which combination best captures those traits?\n"
    "A. Transparent, small-scale, and heavily regulated\n"
    "B. Opaque, scalable, and destructive to people’s lives\n"
    "C. Open source, voluntary, and democratic\n"
    "D. Neutral, purely mathematical, and always fair\n",

    "Q1. In Chapter 1, what is the main danger of relying on mathematical models as WMDs?\n"
    "A. They are always inaccurate because they use too much data\n"
    "B. They are treated as objective, even when their assumptions are biased\n"
    "C. They completely replace all human decision-making\n"
    "D. They only harm wealthy, powerful people\n",

    "Q2. O’Neil becomes disillusioned while working as a Wall Street quant mainly because she realizes that:\n"
    "A. Finance models are too simple to handle real markets\n"
    "B. Her models are being ignored by traders\n"
    "C. Mathematical models are amplifying risk and hurting ordinary people\n"
    "D. The job doesn’t pay enough to justify the long hours\n",

    "Q3. In the chapter on college ranking systems, O’Neil criticizes rankings like U.S. News because they:\n"
    "A. Rely only on student test scores\n"
    "B. Push colleges to “game” the numbers rather than improve education\n"
    "C. Are created entirely by government agencies\n"
    "D. Only apply to elite private universities\n",

    "Q4. Why does O’Neil describe some targeted online advertising as a WMD?\n"
    "A. It always shows users the same ad no matter who they are\n"
    "B. It is too expensive for most companies to use\n"
    "C. It can secretly target vulnerable people with manipulative or predatory messages\n"
    "D. It is required by law for political campaigns\n",

    "Q5. In the criminal justice chapter, what is a major problem with recidivism risk scores used in sentencing?\n"
    "A. They are chosen randomly by judges\n"
    "B. They rely only on biological data like DNA\n"
    "C. They often encode past policing bias, making poor and minority defendants seem riskier\n"
    "D. They are always decided by a public vote\n",

    "Q6. O’Neil argues that algorithmic hiring tools can be WMDs because they:\n"
    "A. Hire everyone who applies, overwhelming HR staff\n"
    "B. Prefer candidates who live far from the workplace\n"
    "C. Filter applicants using hidden criteria that can reproduce discrimination\n"
    "D. Only consider applicants with perfect grades\n",

    "Q7. In the workplace chapter, why are productivity scoring systems especially harmful for low-wage workers?\n"
    "A. Workers can easily edit their own scores\n"
    "B. The systems are fun but distracting\n"
    "C. Workers are closely monitored and punished by scores they can’t see or challenge\n"
    "D. Scores are used only for company games and rewards\n",

    "Q8. When discussing credit scores and lending, O’Neil’s main concern is that:\n"
    "A. Lenders never use data at all\n"
    "B. Credit models are too generous and forgive all debt\n"
    "C. Risk models can trap struggling people in cycles of high-interest debt and exclusion\n"
    "D. Credit scores are calculated by individual judges in court\n",

    "Q9. Why does O’Neil see some insurance pricing models as WMDs?\n"
    "A. They always charge everyone the exact same rate\n"
    "B. They can use proxies (like neighborhood or job) that penalize people for factors beyond their control\n"
    "C. They are designed only for large corporations\n"
    "D. They ignore driving or health records entirely\n",

    "Q10. In the chapter on civic life, what is the key danger of data-driven political targeting?\n"
    "A. Voters gain too much information about candidates\n"
    "B. Campaigns must print fewer paper flyers\n"
    "C. Microtargeted messages can manipulate specific groups without public scrutiny\n"
    "D. It guarantees higher voter turnout in every election\n"
]

# Correct answers (A/B/C/D)
answer_key = [
    "B",  # Q0
    "B",  # Q1
    "C",  # Q2
    "B",  # Q3
    "C",  # Q4
    "C",  # Q5
    "C",  # Q6
    "C",  # Q7
    "C",  # Q8
    "B",  # Q9
    "C"   # Q10
]

score = 0

for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer (A, B, C, or D): ")
    user_answer = user_answer.strip().upper()

    if user_answer == answer_key[i]:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect.\n")

print("You got", score, "out of", len(questions), "correct.")

