# Four Seconds: Interactive Two Layers

The interactive adaptation lives at `/experience/`. Its source is the ten files
in `novel/layers-chapters/`; build the complete reader data with
`python3 novel/build_experience.py`. The existing readers remain available.

Conservation law: all ten chapters, in both timelines, remain reachable in full;
choices change what the reader notices, never the manuscript's events.

Design read: a Bangkok night interrupted by a phone that knows the reader,
opening into the clinical room on the other side of that attention.
Register: cinematic Editorial. Real references: the incoming-message form in
*A Normal Lost Phone*, the physical reveal in Tender Claws' *Pry*, and the light
across Hopper's *Nighthawks*. Use the existing credited paintings. One dominant
scene per screen; phone and controls remain subordinate to it. Heavy display
type, a 2px contact line, and 1px documentary rules serve different purposes.

Interaction: ten scenes; inspectable evidence; optional archive reveal; a
notebook of what the reader chose to preserve; philosophical videos inside
the phone; the offer of an easier account; a twelve-centimetre reach; four
seconds in which the clocks agree. The narrative clock is an illustration,
not a medical readout or a timer that removes access to content.

Keyboard/touch parity, reduced motion, optional synthesized sound after a
user gesture, no autoplay video, safe local-storage fallback. The final reach
can be activated with a button as well as a slider. Full-text passages and
unresolved questions remain visible in the source reader.

Verification: five manuscript preservation tests and five JavaScript state tests
pass. The full ten-encounter route, both complete-text dialogs, optional video
playback, archive transitions, sound toggle, keyboard slider, alternate reach
button, four-second ending, reload/resume, and notebook-preserving replay were
checked in the browser. Layouts were inspected at 1280, 390, and 320 pixels.
The prescribed `axiom-audit` command could not run: the package registry returns
404 for `axiom-audit`. The browser's download-event API timed out, but the actual
exported Markdown file was verified in Downloads with all 16 test entries.
