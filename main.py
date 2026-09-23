import os
import textwrap
import re
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class VideoScript(VoiceoverScene):
    def construct(self):
        # Set up Google TTS (Cloud runners have different IPs, avoiding rate limit)
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
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

        chunk_index_str = os.environ.get("CHUNK_INDEX")
        if chunk_index_str is None:
            # Fallback for local testing
            chunk_index = 0
        else:
            chunk_index = int(chunk_index_str)
            
        if chunk_index < 0 or chunk_index >= len(chunks):
            return
            
        text_content = chunks[chunk_index]
        
        # Split chunk into sentences for punchy kinetic typography
        sentences = re.split(r'(?<=[.!?]) +', text_content)
        
        for sentence in sentences:
            if not sentence.strip():
                continue
                
            # Generate AI audio for the sentence and capture its exact spoken duration
            with self.voiceover(text=sentence) as tracker:
                # Format text beautifully like a graphic designer
                wrapped = textwrap.fill(sentence, width=22)
                
                txt_obj = Text(wrapped, font="Arial", font_size=55, weight=BOLD, line_spacing=1.2)
                txt_obj.set_color(WHITE)
                
                # Drop shadow for professional contrast
                shadow = Text(wrapped, font="Arial", font_size=55, weight=BOLD, line_spacing=1.2)
                shadow.set_color(BLACK).set_opacity(0.8).shift(DOWN*0.05 + RIGHT*0.05)
                
                group = VGroup(shadow, txt_obj)
                group.scale(0.8)
                
                # Math for smooth timing based strictly on the AI voice speed
                dur = tracker.duration
                fade_in_time = min(0.3, dur * 0.2)
                fade_out_time = min(0.3, dur * 0.2)
                zoom_time = dur - fade_in_time - fade_out_time
                
                # 1. Slide up and fade in
                self.play(FadeIn(group, shift=UP*0.3), run_time=fade_in_time)
                # 2. Slow cinematic zoom-in while speaking
                self.play(group.animate.scale(1.15), run_time=zoom_time, rate_func=linear)
                # 3. Fade out before next sentence
                self.play(FadeOut(group, shift=UP*0.3), run_time=fade_out_time)
