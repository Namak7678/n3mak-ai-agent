from fpdf import FPDF

BLUEPRINTS = [
 ("Customer support assistant that never sleeps",
  "A 3-person shop answers the same 20 questions daily on WhatsApp.",
  "Connect the shop's number to an AI assistant trained on the product list, FAQ and delivery policy. It answers instantly, and hands over to a human when it detects anger or a refund request.",
  "WhatsApp Business API + an LLM + a 2 page knowledge file",
  "You are a support agent for {COMPANY}. Answer in the customer's language, max 4 lines. Use only the facts in the attached knowledge file. If unsure or if the customer mentions refund or legal, reply that a human will follow up and tag the chat.",
  "1 day to deploy, 20 minutes per week to keep the knowledge file current.",
  "$400 setup + $120/month"),
 ("Invoice and receipt automation",
  "Receipts arrive as photos in chat and get retyped into a spreadsheet.",
  "Forward every receipt photo to a bot. It reads the total, vendor, date and tax, then appends a row to a spreadsheet and files the image in a dated folder.",
  "Telegram bot + vision LLM + Google Sheets",
  "Read this receipt image. Return only JSON: vendor, date (YYYY-MM-DD), total, currency, tax, category. If a field is unreadable return null for it.",
  "Half a day. Saves 3 to 5 hours a week.",
  "$250 setup + $60/month"),
 ("Lead qualifier in Telegram",
  "Inbound messages are answered hours later and half of them go cold.",
  "A bot asks 4 qualifying questions, scores the lead 1 to 10, and pushes qualified ones to the owner with a one line summary. Cold ones get a polite template answer.",
  "Telegram bot + LLM + a simple database",
  "You are a sales qualifier for {COMPANY}. Ask these 4 questions one at a time: need, budget range, timeline, decision maker. Then output a score from 1 to 10 and a 25 word summary for the owner.",
  "1 day. First reply drops from hours to seconds.",
  "$350 setup + $100/month"),
 ("Content engine for one niche",
  "Posting stops whenever the owner gets busy.",
  "A weekly job generates 7 posts from a single source article plus the brand voice file, and schedules them.",
  "An LLM + a scheduler + a brand voice file",
  "Write 7 short posts for {BRAND} from this article. Voice: {VOICE}. No hashtags, no emojis, max 60 words each, one clear takeaway per post.",
  "2 hours once, then fully automatic.",
  "$300 setup + $80/month"),
 ("Quote generator from a chat",
  "Quotes take 40 minutes each and are inconsistent.",
  "Owner sends requirements in chat, the assistant returns a formatted quote with line items, terms and a validity date, ready to send.",
  "Telegram bot + LLM + a price table file",
  "Build a quote for {COMPANY} from this request. Use only prices from the price table. Output: item, quantity, unit price, line total, subtotal, tax, total, validity 14 days. Never invent a discount.",
  "1 day. Cuts quote time to under 3 minutes.",
  "$350 setup + $90/month"),
 ("Watchdog for competitor prices",
  "Prices change silently and margins erode.",
  "A daily check reads 5 competitor pages, records changes, and alerts only when a price moves more than 5 percent.",
  "A scraper job + a database + an alert bot",
  "Extract product name, price and currency as JSON from this page. Return an empty array if the page has no prices.",
  "1 day. Alerts only when something matters.",
  "$300 setup + $70/month"),
 ("Onboarding sequence for new clients",
  "New clients get forgotten in the first week, then churn.",
  "On signup, a sequence sends 4 messages over 10 days, each with one action, and stops automatically when the client replies.",
  "A form + a scheduled bot + a stop condition",
  "Write message {N} of 4 for a new {SERVICE} client. Goal: one small action. Max 3 sentences. No sales pitch.",
  "Half a day. Reduces first month churn.",
  "$250 setup + $60/month"),
 ("Meeting notes to action items",
  "Meetings end without assigned tasks.",
  "Upload a recording or transcript, receive a summary plus tasks with owner and due date, pushed into the task board.",
  "Transcription + LLM + task board API",
  "From this transcript, output: 5 line summary, decisions, and tasks as JSON with owner, task, due date. Mark missing owners as UNASSIGNED.",
  "1 day. Removes manual note taking.",
  "$300 setup + $70/month"),
 ("Multilingual product support",
  "Foreign customers write in English and nobody answers fast.",
  "Every inbound message is auto translated to the owner's language, answered, then translated back in the customer's language.",
  "Bot + LLM translation layer",
  "Detect the language, answer in that language, and also give the owner a one line translation of the customer request.",
  "Half a day. Opens cross border sales.",
  "$250 setup + $60/month"),
 ("Weekly numbers digest",
  "The owner never looks at dashboards.",
  "Every Monday at 8am the assistant pulls sales, orders and messages from the last week, writes 5 bullet points and sends them in chat with one recommended action.",
  "Two data sources + LLM + a scheduled job",
  "Write a 5 bullet weekly digest from this data for the owner. Last bullet must be one concrete action to take this week, based on the numbers only.",
  "1 day. One message replaces a dashboard.",
  "$250 setup + $60/month"),
]

PRICING = [
 ("What you charge", "How to justify it"),
 ("$250 to $400 setup", "One automation replaces 3 to 5 hours of weekly manual work."),
 ("$60 to $120 monthly", "Hosting plus upkeep. It is a subscription, not a favour."),
 ("$900 to $1,500 bundle", "Three blueprints together, sold as a starter system."),
]

pdf = FPDF(format="A4")
_mc = None
pdf.set_auto_page_break(auto=True, margin=18)

def MC(h, text, **kw):
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0, h, text, **kw)


# Cover
pdf.add_page()
pdf.set_font("Helvetica", "B", 30)
pdf.ln(60)
MC(12, "10 AI Automation\nBlueprints for\nSmall Business", align="C")
pdf.ln(6)
pdf.set_font("Helvetica", "", 13)
MC(8, "Ready to sell, ready to build. Each one fits in a single day\nand earns a monthly fee.", align="C")
pdf.ln(14)
pdf.set_font("Helvetica", "B", 11)
MC(7, "N3mak Services", align="C")
pdf.set_font("Helvetica", "", 9)
MC(6, "You may use these blueprints in your own client work.\nDo not resell the document itself.", align="C")

# How to use
pdf.add_page()
pdf.set_font("Helvetica", "B", 18)
MC(9, "How to use this pack")
pdf.ln(3)
pdf.set_font("Helvetica", "", 11)
steps = [
 "1. Pick the blueprint that matches a business you already know.",
 "2. Copy the prompt, replace {COMPANY} and the knowledge file with real data.",
 "3. Build it once, test it on 20 real messages.",
 "4. Charge a setup fee plus a monthly fee. Never sell it as a one off.",
 "5. Keep the knowledge file current. That upkeep is what the monthly fee pays for.",
]
for s in steps:
    MC(7, s)
    pdf.ln(1)
pdf.ln(3)
pdf.set_font("Helvetica", "B", 12)
MC(7, "The one rule that decides success")
pdf.set_font("Helvetica", "", 11)
MC(7, "Sell the outcome, not the technology. A shop owner does not buy an LLM. They buy 'my messages get answered in seconds and I stop losing orders at night'.")

# Blueprints
for i, (title, pain, sol, stack, prompt, time, price) in enumerate(BLUEPRINTS, 1):
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(150, 80, 60)
    MC(6, f"BLUEPRINT {i:02d}")
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "B", 17)
    MC(9, title)
    pdf.ln(2)

    def block(label, text, mono=False):
        pdf.set_font("Helvetica", "B", 10)
        MC(6, label)
        pdf.set_font("Courier" if mono else "Helvetica", "", 10)
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0, 5 if mono else 6, text)
        pdf.ln(2.5)

    block("The pain", pain)
    block("The fix", sol)
    block("Stack", stack)
    block("Prompt to copy", prompt, mono=True)
    block("Deploy time", time)
    block("What to charge", price)

# Pricing page
pdf.add_page()
pdf.set_font("Helvetica", "B", 18)
MC(9, "Pricing that sticks")
pdf.ln(3)
pdf.set_font("Helvetica", "B", 11)
MC(7, "Item".ljust(38) + "Reason")
pdf.set_font("Helvetica", "", 10)
for a, b in PRICING[1:]:
    MC(7, f"{a}  -  {b}")
pdf.ln(4)
pdf.set_font("Helvetica", "B", 12)
MC(7, "First client script")
pdf.set_font("Helvetica", "", 10)
MC(6, "Hi {NAME}, I built an assistant that answers your WhatsApp questions in seconds and hands over the big ones to you. It takes one day to set up and costs {PRICE} to start, {MONTHLY} after. Want me to set it up on your real messages this week and you keep it only if it works?")
pdf.ln(6)
pdf.set_font("Helvetica", "B", 9)
MC(6, "N3mak Services  -  AI automation for small business  -  t.me/N3mak_bot")

pdf.output("AI-Automation-Blueprints.pdf")
print("pages:", pdf.pages_count)
