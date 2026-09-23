import os
import textwrap
from manim import *

class VideoScript(Scene):
    def construct(self):
        chunks = [
            "Your emotions are not your friend. Let me say that again. Your emotions are not your friend. They are not some sacred inner voice guiding you toward truth and happiness. They are biological reactions designed for a world that no longer exists. A world where immediate emotional responses meant the difference between life and death.",
            "But in today's world, your emotional reactions are sabotaging your success, destroying your relationships and keeping you trapped in cycles of regret and failure. Every single day, you make decisions based on how you feel in the moment. You get triggered by a comment and fire back with something you'll regret. You feel overwhelmed and quit on your goals. You get anxious about a presentation and avoid the opportunity that could change your career.",
            "You let anger control your words and destroy relationships that took years to build. You are being controlled by chemical reactions in your brain. And you don't even realize it. But here's what the top 1% of high achievers know that you don't. They have learned the most powerful skill in human existence. the ability to not react, the ability to feel the emotion, acknowledge it, and then choose their response based on logic,",
            "strategy, and long-term thinking instead of the primitive impulses screaming in their heads. This is not about becoming emotionless. This is not about suppressing your feelings or pretending they don't exist. This is about taking back control of your life by mastering the space between stimulus and response. The space where your power lives. The space where your future is determined.",
            "By the time you finish this audio book, you will never be the same person who started listening. You will have the tools, the knowledge, and the mental frameworks to control your emotions instead of being controlled by them. You will learn how to stay calm under pressure, make better decisions when stakes are high, and build the kind of unshakable inner strength that separates winners from everyone else. Chapter 1.",
            "The hidden cost of emotional reactivity. Most people have no idea how much their emotional reactions are costing them. They think it's normal to get triggered. They think it's human nature to lose control when things get difficult. They think that strong emotions are a sign of passion and authenticity. They are wrong. Dead wrong. And this delusion is destroying their lives in ways they can't even see. Let me paint you a picture of what emotional reactivity actually looks like in the real world.",
            "You're in a meeting with your boss and colleagues. Someone challenges your idea in a way that feels disrespectful. Your heart starts racing. Your face gets hot. The voice in your head starts screaming about how unfair this is. How they don't understand your vision. How they're trying to make you look bad. And before you know it, you're defending yourself with an edge in your voice that makes everyone in the room uncomfortable. You've just damaged your professional reputation over a 60-second emotional reaction.",
            "Or maybe you're having an argument with your partner about something relatively minor. They say something that hits a nerve. Instead of staying calm and working toward a solution, you escalate. You bring up past grievances. You say things designed to hurt them because you're hurting. 10 minutes later, you've turned a small disagreement into a relationship threatening fight that will take days to recover from. All because you couldn't control your initial emotional reaction.",
            "Here's the brutal truth that no one wants to face. Every time you react emotionally instead of responding thoughtfully, you are training your brain to be weaker. You are reinforcing neural pathways that make you more likely to lose control the next time. You are literally rewiring your brain for failure, for conflict, for regret. And the worst part is that you're doing it voluntarily. The science is clear on this.",
            "Every emotional reaction triggers the release of stress hormones like cortisol and adrenaline. These chemicals flood your system, cloud your judgment, and make it impossible to think clearly. But here's what most people don't realize. These hormones don't just disappear when the situation is over. They stay in your system for hours, sometimes days, affecting every decision you make, every interaction you have, every thought that crosses your mind.",
            "This means that one emotional reaction in the morning can sabotage your entire day. That argument with your spouse affects how you perform at work. That stressful email triggers a cascade of poor decisions that ripple through your entire week. You become trapped in a cycle of reactivity where each emotional outburst makes the next one more likely. But the cost goes deeper than just your daily performance.",
            "Chronic emotional reactivity literally changes your brain structure. Studies using brain imaging technology show that people who regularly lose emotional control have smaller prefrontal cortexes. This is the part of your brain responsible for rational thinking, planning, and impulse"
        ]

        # Read the environment variable to know which chunk to render
        chunk_index_str = os.environ.get("CHUNK_INDEX")
        if chunk_index_str is None:
            print("No CHUNK_INDEX found. Please run with CHUNK_INDEX environment variable set.")
            return

        chunk_index = int(chunk_index_str)
        if chunk_index < 0 or chunk_index >= len(chunks):
            print(f"Invalid CHUNK_INDEX: {chunk_index}")
            return
            
        text_content = chunks[chunk_index]
        
        # Wrap text so it fits on screen nicely
        wrapped_text = "\n".join(textwrap.wrap(text_content, width=40))
        
        # Create text Mobject with nice formatting
        t = Text(wrapped_text, font="Arial", font_size=36, line_spacing=1.5, weight=BOLD)
        t.set_color(WHITE)
        
        # We want the video to be roughly 30 seconds.
        # Write animation takes 24 seconds, followed by 5 seconds of wait, and 1 second fade out.
        self.play(Write(t), run_time=24)
        self.wait(5)
        self.play(FadeOut(t), run_time=1)
