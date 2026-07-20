"""Notification template catalog — Traguin notification templates."""

from __future__ import annotations

from dataclasses import dataclass

TEMPLATE_IDS = (
    "customer_inquiry_received",
    "customer_enquiry_welcome",
    "team_new_lead",
    "team_lead_assigned",
    "team_rm_accept_reminder",
    "team_no_action_after_accept",
    "customer_itinerary_sent",
    "customer_quote",
    "customer_booking_confirmed",
    "team_booking_confirmed",
    "customer_payment_invoice",
    "customer_payment_overdue",
    "customer_payment_receipt",
    "customer_travel_documents",
    "customer_pre_departure",
    "customer_trip_complete",
    "team_dump_lead",
    "team_payment_overdue",
    "team_escalation",
)


@dataclass(frozen=True)
class NotificationTemplate:
    id: str
    subject: str
    email_body_html: str
    whatsapp_text: str | None = None
    plain_body: str | None = None
    hero_title: str | None = None
    hero_subtitle: str | None = None
    hero_border_color: str = "#C9A227"
    hero_bg: str | None = None
    email_subheader: str = "Curated Journeys · Seamless Experiences"
    wrap_layout: bool = True


_REF = (
    '<div style="background:linear-gradient(135deg,#f0f6fc,#fff);border:1px solid #d8e2ec;'
    'border-left:4px solid #1E6BB8;border-radius:8px;padding:14px 16px;margin:12px 0;">'
    '<div style="font-size:11px;color:#5a6b7d;text-transform:uppercase;">{label}</div>'
    '<div style="font-size:18px;font-weight:700;color:#0B3D6E;margin-top:4px;">{{value}}</div>{extra}</div>'
)


def _ref(label: str, value_key: str, extra: str = "") -> str:
    extra_html = f'<div style="font-size:12px;color:#5a6b7d;margin-top:4px;">{extra}</div>' if extra else ""
    return _REF.format(label=label, extra=extra_html).replace("{value}", f"{{{{{value_key}}}}}")


_GRID = """<table width="100%" cellpadding="0" cellspacing="0" style="margin:12px 0;font-size:13px;">
<tr><td width="50%" style="padding:4px 8px 4px 0;"><div style="font-size:11px;color:#5a6b7d;text-transform:uppercase;">{l1}</div><div style="font-weight:600;">{{v1}}</div></td>
<td width="50%"><div style="font-size:11px;color:#5a6b7d;text-transform:uppercase;">{l2}</div><div style="font-weight:600;">{{v2}}</div></td></tr>
<tr><td style="padding:4px 8px 4px 0;"><div style="font-size:11px;color:#5a6b7d;text-transform:uppercase;">{l3}</div><div style="font-weight:600;">{{v3}}</div></td>
<td><div style="font-size:11px;color:#5a6b7d;text-transform:uppercase;">{l4}</div><div style="font-weight:600;">{{v4}}</div></td></tr>
</table>"""


def _grid(rows: list[tuple[str, str]]) -> str:
    if len(rows) < 4:
        rows = rows + [("—", "—")] * (4 - len(rows))
    l1, k1 = rows[0]
    l2, k2 = rows[1] if len(rows) > 1 else ("—", "—")
    l3, k3 = rows[2] if len(rows) > 2 else ("—", "—")
    l4, k4 = rows[3] if len(rows) > 3 else ("—", "—")
    return (
        _GRID.format(l1=l1, l2=l2, l3=l3, l4=l4)
        .replace("{v1}", f"{{{{{k1}}}}}")
        .replace("{v2}", f"{{{{{k2}}}}}")
        .replace("{v3}", f"{{{{{k3}}}}}")
        .replace("{v4}", f"{{{{{k4}}}}}")
    )


_TEMPLATES: dict[str, NotificationTemplate] = {}


def _register(spec: NotificationTemplate) -> None:
    _TEMPLATES[spec.id] = spec


_register(
    NotificationTemplate(
        id="customer_inquiry_received",
        subject="We received your travel enquiry — Traguin Travel",
        hero_title="Hello, {{Customer_Name}}!",
        hero_subtitle="Thank you for your interest in Traguin Travel.",
        email_body_html=(
            "<p>We have successfully received your enquiry.</p>"
            "<p>Our travel expert will review your requirements and get in touch with you "
            "shortly to help you plan your perfect trip.</p>"
            "<p>If you have any urgent questions, simply reply to this email or WhatsApp us at "
            "<strong>{{Support_Phone}}</strong>.</p>"
            "<p>Thank you for choosing Traguin!</p>"
        ),
        whatsapp_text="""👋 Hello {{Customer_Name}},
Thank you for your interest in Traguin Travel! 🌍
We have successfully received your enquiry.
Our travel expert will review your requirements and get in touch with you shortly to help you plan your perfect trip.
If you have any urgent questions, simply reply to this message. We're happy to assist you.
Thank you for choosing Traguin! ✈️""",
    )
)

_register(
    NotificationTemplate(
        id="customer_enquiry_welcome",
        subject="Your travel enquiry is confirmed — Ref {{Temp_ID}}",
        hero_title="Thank you, {{Customer_Name}}!",
        hero_subtitle="We've received your travel enquiry and assigned a dedicated travel expert to you.",
        email_body_html=_ref("Enquiry Reference", "Temp_ID")
        + _grid(
            [
                ("Destination", "Destination"),
                ("Travel Dates", "Travel_Dates"),
                ("Travellers", "Guests"),
                ("Your Expert", "RM_Name"),
            ]
        )
        + "<p>Your Relationship Manager will contact you shortly to understand your preferences and craft a personalised itinerary.</p>"
        + '<div style="background:#eff6ff;border:1px solid #93c5fd;border-radius:6px;padding:12px;margin:12px 0;font-size:13px;color:#1e40af;">Need help? Reply to this email or WhatsApp us at <strong>{{Support_Phone}}</strong></div>',
        whatsapp_text="""✈️ *Welcome to Traguin, {{Customer_Name}}!*

Your travel enquiry has been registered.

📋 Ref: *{{Temp_ID}}*
🌍 Destination: {{Destination}}
📅 Dates: {{Travel_Dates}}
👤 Your expert: *{{RM_Name}}*

We'll call you shortly to plan your perfect trip.

_Traguin — Curated Journeys_""",
    )
)

_register(
    NotificationTemplate(
        id="team_new_lead",
        subject="[Traguin CRM] New Lead — {{Customer_Name}} · {{Temp_ID}}",
        email_subheader="Internal · Operations Alert",
        hero_title="New Enquiry Captured",
        hero_subtitle="Priority: {{Priority}} · Enquiry #{{Inquiry_Count}} from this mobile",
        hero_border_color="#f59e0b",
        email_body_html=_ref("Temp ID", "Temp_ID")
        + _grid(
            [
                ("Customer", "Customer_Name"),
                ("Mobile", "Phone"),
                ("Destination", "Destination"),
                ("Travel Date", "Travel_Dates"),
                ("Source (internal)", "Source_Code"),
                ("Budget", "Budget"),
            ]
        )
        + '<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:6px;padding:12px;margin:12px 0;font-size:13px;">🔄 <strong>Active enquiries from same mobile:</strong> {{Active_Enquiry_1}}, {{Active_Enquiry_2}}<br>🏷️ <strong>Customer flags:</strong> {{Customer_Flags}}</div>'
        + '<div style="text-align:center;margin:16px 0;"><a href="{{CRM_Link}}" style="display:inline-block;background:#1E6BB8;color:#fff;text-decoration:none;padding:10px 22px;border-radius:6px;font-weight:600;">Open in CRM →</a></div>',
        whatsapp_text="""🔔 *New Lead*

Ref: {{Temp_ID}}
👤 {{Customer_Name}}
📞 {{Phone}}
✈️ {{Destination}} · {{Travel_Dates}}
🔥 Priority: *{{Priority}}*
📊 Enquiry #{{Inquiry_Count}}

🔄 Active: {{Active_Enquiry_1}} | {{Active_Enquiry_2}}
🏷️ {{Customer_Flags}}

🔗 {{CRM_Link}}""",
    )
)

_register(
    NotificationTemplate(
        id="team_lead_assigned",
        subject="Action Required — New lead assigned · Accept within 15 min",
        email_subheader="Lead Assignment · Action required",
        hero_title="Hi {{RM_Name}}, a lead needs your attention",
        hero_subtitle="Please accept or reject within 15 minutes (working hours)",
        hero_border_color="#b91c1c",
        email_body_html=_ref("Reference", "Temp_ID")
        + _grid(
            [
                ("Customer", "Customer_Name"),
                ("Phone", "Phone"),
                ("Destination", "Destination"),
                ("Dates", "Travel_Dates"),
                ("Priority", "Priority"),
                ("Enquiry #", "Inquiry_Count"),
            ]
        )
        + '<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:6px;padding:12px;margin:12px 0;font-size:13px;">🔄 Other active enquiries: {{Active_Enquiry_1}} · {{Active_Enquiry_2}}<br>🏷️ Flags: {{Customer_Flags}}</div>'
        + '<div style="text-align:center;margin:16px 0;"><a href="{{Accept_Link}}" style="display:inline-block;background:#0d7a4e;color:#fff;text-decoration:none;padding:10px 20px;border-radius:6px;font-weight:600;margin:4px;">✓ Accept Lead</a> <a href="{{Reject_Link}}" style="display:inline-block;background:#fff;color:#b91c1c;text-decoration:none;padding:9px 18px;border-radius:6px;font-weight:600;border:2px solid #b91c1c;margin:4px;">✕ Reject Lead</a></div>'
        + '<p style="text-align:center;font-size:12px;color:#5a6b7d;">Or open full details in CRM</p>'
        + '<div style="text-align:center;"><a href="{{CRM_Link}}" style="color:#1E6BB8;">View in CRM →</a></div>',
        whatsapp_text="""📋 *Lead Assigned to You*

{{Customer_Name}} · {{Phone}}
✈️ {{Destination}} · {{Travel_Dates}}
🔥 {{Priority}} · Enquiry #{{Inquiry_Count}}
Ref: {{Temp_ID}}

⏱ Accept within *15 min* (working hrs)

✅ Accept: {{Accept_Link}}
❌ Reject: {{Reject_Link}}""",
    )
)

_register(
    NotificationTemplate(
        id="team_rm_accept_reminder",
        subject="⏰ Reminder — Lead {{Temp_ID}} awaiting your acceptance",
        hero_title="",
        hero_subtitle="",
        email_body_html='<div style="background:#fef2f2;border:1px solid #fecaca;border-radius:6px;padding:12px;margin:0 0 12px;color:#991b1b;">⚠️ <strong>{{Elapsed_Time}}</strong> have passed since lead {{Temp_ID}} was assigned to you.</div>'
        + "<p>Customer <strong>{{Customer_Name}}</strong> is waiting. Please accept or reject immediately.</p>"
        + '<div style="text-align:center;margin:16px 0;"><a href="{{Accept_Link}}" style="display:inline-block;background:#0d7a4e;color:#fff;text-decoration:none;padding:10px 20px;border-radius:6px;font-weight:600;margin:4px;">✓ Accept Lead</a> <a href="{{Reject_Link}}" style="display:inline-block;background:#fff;color:#b91c1c;text-decoration:none;padding:9px 18px;border-radius:6px;font-weight:600;border:2px solid #b91c1c;margin:4px;">✕ Reject Lead</a></div>',
        whatsapp_text="""⏰ *Reminder — {{Elapsed_Time}}*

Lead {{Temp_ID}} still pending.
👤 {{Customer_Name}} · {{Phone}}

Please Accept or Reject now.
✅ {{Accept_Link}} · ❌ {{Reject_Link}}""",
        wrap_layout=True,
    )
)

_register(
    NotificationTemplate(
        id="team_no_action_after_accept",
        subject="Follow-up needed — {{Customer_Name}} · {{Temp_ID}}",
        email_body_html="<p>You accepted lead <strong>{{Temp_ID}}</strong> 30 minutes ago but no call or note has been logged.</p>"
        + "<p>Please contact <strong>{{Customer_Name}}</strong> at {{Phone}} now.</p>"
        + '<div style="text-align:center;margin:16px 0;"><a href="{{CRM_Link}}" style="display:inline-block;background:#1E6BB8;color:#fff;text-decoration:none;padding:10px 22px;border-radius:6px;font-weight:600;">Start Call in CRM →</a></div>',
        whatsapp_text="""⚠️ *Action Required*

You accepted {{Temp_ID}} 30 min ago.
No call logged yet.

📞 Please call {{Customer_Name}}: {{Phone}}
🔗 {{CRM_Link}}""",
    )
)

_register(
    NotificationTemplate(
        id="customer_itinerary_sent",
        subject="Your personalised itinerary is ready — {{Destination}}",
        email_subheader="Itinerary Preview",
        hero_title="Your dream trip to {{Destination}}",
        hero_subtitle="Prepared exclusively for you by {{RM_Name}}",
        email_body_html=_ref("Enquiry Reference", "Temp_ID")
        + _grid(
            [
                ("Duration", "Nights"),
                ("Travellers", "Guests"),
                ("Travel Dates", "Travel_Dates"),
                ("Trip Type", "Holiday_Type"),
            ]
        )
        + "<p>Please review the day-wise plan in the attached PDF. Once you approve the itinerary, we'll share the detailed quotation.</p>"
        + '<div style="background:#eff6ff;border:1px solid #93c5fd;border-radius:6px;padding:12px;margin:12px 0;">📎 Attachment: Traguin_Itinerary_{{Temp_ID}}.pdf</div>',
        whatsapp_text="""✈️ *Your Itinerary is Ready!*

🌍 {{Destination}}
📅 {{Travel_Dates}}
👥 {{Guests}} Guests

Hi {{Customer_Name}}, your personalised plan is attached.

Please review and let us know:
✅ Approve — reply *YES*
✏️ Changes — tell us what to adjust

_Pricing will be shared after itinerary approval._

— {{RM_Name}}, Traguin""",
    )
)

_register(
    NotificationTemplate(
        id="customer_quote",
        subject="Your Traguin quotation — {{Destination}} · {{Temp_ID}}",
        email_subheader="Quotation · Approved by Accounts",
        hero_title="Your trip quotation is ready",
        hero_subtitle="Based on your approved itinerary",
        hero_border_color="#C9A227",
        email_body_html=_ref("Package Total", "Total_Amount").replace("#1E6BB8", "#C9A227")
        + _grid(
            [
                ("Destination", "Destination"),
                ("Travel Dates", "Travel_Dates"),
                ("Inclusions", "Inclusions_Summary"),
                ("Valid Until", "Quote_Valid_Till"),
            ]
        )
        + "<p>Full quotation PDF attached. Payment schedule will be shared upon confirmation.</p>",
        whatsapp_text="""💰 *Your Quotation — {{Destination}}*

Ref: {{Temp_ID}}
📅 {{Travel_Dates}}
💵 Package: *₹{{Total_Amount}}*

Inclusions: {{Inclusions_Summary}}
Valid till: {{Quote_Valid_Till}}

Reply *CONFIRM* to proceed with booking.

— {{RM_Name}}, Traguin""",
    )
)

_register(
    NotificationTemplate(
        id="customer_booking_confirmed",
        subject="Booking Confirmed — {{Destination}} · {{Customer_ID}}",
        email_subheader="Booking Confirmation",
        hero_title="✓ Booking Confirmed",
        hero_subtitle="Your journey to {{Destination}} is officially booked!",
        hero_border_color="#0d7a4e",
        hero_bg="linear-gradient(180deg,#f0fdf4,#fff)",
        email_body_html=_ref("Customer ID", "Customer_ID", "Booking ID: {{Booking_ID}}").replace("#1E6BB8", "#0d7a4e")
        + _grid(
            [
                ("Passenger / Lead", "Customer_Name"),
                ("Destination", "Destination"),
                ("Departure", "Travel_Start"),
                ("Return", "Travel_End"),
                ("Travellers", "Guests"),
                ("Package Value", "Total_Amount"),
                ("Relationship Manager", "RM_Name"),
                ("Status", "Status_Label"),
            ]
        )
        + '<div style="background:#eff6ff;border:1px solid #93c5fd;border-radius:6px;padding:12px;margin:12px 0;">Payment schedule and invoices will follow shortly from our Accounts team.</div>',
        whatsapp_text="""✅ *Booking Confirmed!*

Dear {{Customer_Name}},

Your trip to *{{Destination}}* is confirmed.

🆔 Customer ID: *{{Customer_ID}}*
📋 Booking: {{Booking_ID}}
📅 {{Travel_Start}} → {{Travel_End}}
👥 {{Guests}} Guests
💵 ₹{{Total_Amount}}

Your Traguin expert {{RM_Name}} will guide you through the next steps.

_Traguin — Curated Journeys_""",
    )
)

_register(
    NotificationTemplate(
        id="team_booking_confirmed",
        subject="[Traguin] New Booking — {{Customer_ID}} · {{Destination}}",
        email_subheader="Internal · New Booking",
        email_body_html=_ref("Temp ID", "Temp_ID", "Customer ID: {{Customer_ID}}")
        + _grid(
            [
                ("Customer", "Customer_Name"),
                ("RM", "RM_Name"),
                ("Destination", "Destination"),
                ("Amount", "Total_Amount"),
                ("Travel", "Travel_Dates"),
                ("Booking ID", "Booking_ID"),
            ]
        )
        + "<p><strong>Account:</strong> Set payment schedule with RM.<br><strong>Operations:</strong> Await payment clearance before supplier booking.</p>"
        + '<div style="text-align:center;"><a href="{{CRM_Link}}" style="display:inline-block;background:#1E6BB8;color:#fff;text-decoration:none;padding:10px 22px;border-radius:6px;font-weight:600;">Open Booking in CRM →</a></div>',
        whatsapp_text=None,
    )
)

_register(
    NotificationTemplate(
        id="customer_payment_invoice",
        subject="Invoice {{Invoice_No}} — Payment due {{Due_Date}}",
        email_subheader="Invoice",
        email_body_html=_ref("Amount Due", "Due_Amount")
        + _grid(
            [
                ("Invoice No.", "Invoice_No"),
                ("Due Date", "Due_Date"),
                ("Customer ID", "Customer_ID"),
                ("Booking", "Booking_ID"),
            ]
        )
        + '<div style="text-align:center;"><a href="{{Payment_Link}}" style="display:inline-block;background:#C9A227;color:#0B3D6E;text-decoration:none;padding:10px 22px;border-radius:6px;font-weight:600;">Pay Now →</a></div>'
        + "<p style=\"font-size:13px;color:#5a6b7d;\">UPI · Bank Transfer · Card accepted. RM {{RM_Name}} is copied for any queries.</p>",
        whatsapp_text="""🧾 *Payment Invoice*

Customer ID: {{Customer_ID}}
Invoice: {{Invoice_No}}
💵 Amount: *₹{{Due_Amount}}*
📅 Due: {{Due_Date}}
✈️ {{Destination}}

Pay here: {{Payment_Link}}

For queries contact {{RM_Name}}.
— Traguin Accounts""",
    )
)

_register(
    NotificationTemplate(
        id="customer_payment_overdue",
        subject="Payment reminder — Invoice {{Invoice_No}} overdue",
        email_body_html='<div style="background:#fef2f2;border:1px solid #fecaca;border-radius:6px;padding:12px;margin:0 0 12px;color:#991b1b;">Your payment of <strong>₹ {{Due_Amount}}</strong> for {{Destination}} was due on <strong>{{Due_Date}}</strong>.</div>'
        + "<p>Dear {{Customer_Name}}, please complete payment to avoid disruption to your travel plans. Your booking may be placed on hold until payment is received.</p>"
        + '<div style="text-align:center;"><a href="{{Payment_Link}}" style="display:inline-block;background:#b91c1c;color:#fff;text-decoration:none;padding:10px 22px;border-radius:6px;font-weight:600;">Pay Now →</a></div>'
        + "<p style=\"font-size:13px;color:#5a6b7d;\">Need assistance? Contact {{RM_Name}} at {{RM_Phone}}.</p>",
        whatsapp_text="""⚠️ *Payment Reminder*

Hi {{Customer_Name}},
Invoice {{Invoice_No}} is overdue.

💵 ₹{{Due_Amount}} · Due {{Due_Date}}
✈️ {{Destination}}

Please pay: {{Payment_Link}}
Or contact {{RM_Name}}: {{RM_Phone}}""",
    )
)

_register(
    NotificationTemplate(
        id="customer_payment_receipt",
        subject="Payment received — Receipt {{Receipt_No}}",
        email_subheader="Payment Receipt",
        hero_title="Payment Received ✓",
        hero_subtitle="Thank you for your payment",
        hero_border_color="#0d7a4e",
        email_body_html=_ref("Amount Paid", "Paid_Amount").replace("#1E6BB8", "#0d7a4e")
        + _grid(
            [
                ("Receipt No.", "Receipt_No"),
                ("Date", "Payment_Date"),
                ("Customer ID", "Customer_ID"),
                ("Balance", "Balance_Remaining"),
            ]
        )
        + '<div style="background:#eff6ff;border:1px solid #93c5fd;border-radius:6px;padding:12px;margin:12px 0;">📎 Receipt PDF attached. {{Balance_Message}}</div>',
        whatsapp_text="""✅ *Payment Received*

Receipt: {{Receipt_No}}
💵 ₹{{Paid_Amount}} received
📅 {{Payment_Date}}
🆔 {{Customer_ID}}

Balance: {{Balance_Remaining}}

Thank you, {{Customer_Name}}!
— Traguin Accounts""",
    )
)

_register(
    NotificationTemplate(
        id="customer_travel_documents",
        subject="Your travel documents are ready — {{Destination}}",
        email_subheader="Travel Kit",
        hero_title="Your travel kit is ready!",
        hero_subtitle="Everything you need for {{Destination}}",
        email_body_html=_ref("Booking", "Booking_ID")
        + "<p>Your travel folder includes:</p><ul><li>Flight / transport tickets</li><li>Hotel vouchers</li><li>Visa documents (if applicable)</li><li>Day-wise itinerary &amp; contact numbers</li></ul>"
        + '<div style="text-align:center;"><a href="{{Docs_Link}}" style="display:inline-block;background:#1E6BB8;color:#fff;text-decoration:none;padding:10px 22px;border-radius:6px;font-weight:600;">Download Travel Folder →</a></div>'
        + '<div style="background:#eff6ff;border:1px solid #93c5fd;border-radius:6px;padding:12px;margin:12px 0;">Emergency support: {{Emergency_Phone}} · Available 24×7 during your trip</div>',
        whatsapp_text="""📁 *Travel Documents Ready!*

{{Customer_Name}}, your kit for *{{Destination}}* is ready.

📋 Booking: {{Booking_ID}}
📅 Travel: {{Travel_Start}}

Includes tickets, hotel vouchers & itinerary.
📎 Download: {{Docs_Link}}

24×7 support: {{Emergency_Phone}}
— Traguin Operations""",
    )
)

_register(
    NotificationTemplate(
        id="customer_pre_departure",
        subject="You're almost there — {{Destination}} in {{Days_Left}} days",
        email_body_html="<h3 style=\"color:#0B3D6E;margin-bottom:12px;\">Pre-Departure Checklist</h3><ul><li>✓ Valid passport / ID</li><li>✓ Printed or digital vouchers</li><li>✓ Travel insurance (if purchased)</li><li>✓ Emergency contacts saved</li></ul>"
        + _grid([("Departure", "Travel_Start"), ("RM Contact", "RM_Phone")])
        + "<p>Wishing you a wonderful journey, {{Customer_Name}}!</p>",
        whatsapp_text="""🌟 *{{Days_Left}} days to go!*

Hi {{Customer_Name}},
Your trip to *{{Destination}}* starts {{Travel_Start}}.

Quick checklist:
✅ Passport / ID
✅ Vouchers downloaded
✅ Emergency: {{Emergency_Phone}}

Have a safe & happy journey! ✈️
— {{RM_Name}}, Traguin""",
    )
)

_register(
    NotificationTemplate(
        id="customer_trip_complete",
        subject="Thank you for travelling with Traguin — {{Customer_ID}}",
        hero_title="Thank you, {{Customer_Name}}!",
        hero_subtitle="We hope you had an unforgettable experience in {{Destination}}",
        hero_border_color="#C9A227",
        email_body_html="<p>Your booking <strong>{{Booking_ID}}</strong> is now complete. We'd love to hear about your trip.</p>"
        + '<div style="text-align:center;"><a href="{{Feedback_Link}}" style="display:inline-block;background:#C9A227;color:#0B3D6E;text-decoration:none;padding:10px 22px;border-radius:6px;font-weight:600;margin:4px;">Share Feedback →</a></div>'
        + '<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:6px;padding:12px;margin:12px 0;">Refer a friend and earn rewards on your next Traguin journey!</div>',
        whatsapp_text="""🙏 *Welcome back, {{Customer_Name}}!*

Thank you for choosing Traguin for your *{{Destination}}* trip.

We'd love your feedback:
⭐ {{Feedback_Link}}

Refer a friend & get rewards on your next trip! 🤝

— Team Traguin""",
    )
)

_register(
    NotificationTemplate(
        id="team_dump_lead",
        subject="Lead moved to Dump — {{Temp_ID}} · {{Customer_Name}}",
        email_subheader="Internal",
        email_body_html='<div style="background:#fef2f2;border:1px solid #fecaca;border-radius:6px;padding:12px;margin:0 0 12px;color:#991b1b;">Lead {{Temp_ID}} moved to <strong>Dump</strong> after {{Attempt_Count}} contact attempts with no response.</div>'
        + _grid(
            [
                ("Customer", "Customer_Name"),
                ("RM", "RM_Name"),
                ("Destination", "Destination"),
                ("Last attempt", "Last_Attempt_Date"),
            ]
        ),
        whatsapp_text="""🗑️ *Dump Lead*

{{Temp_ID}} · {{Customer_Name}}
{{Attempt_Count}} attempts — no answer.
RM: {{RM_Name}}

Moved out of active queue.
Nisha to review weekly.""",
    )
)

_register(
    NotificationTemplate(
        id="team_payment_overdue",
        subject="[Alert] Payment overdue — {{Customer_ID}} · ₹{{Due_Amount}}",
        email_subheader="Accounts Alert",
        email_body_html='<div style="background:#fef2f2;border:1px solid #fecaca;border-radius:6px;padding:12px;margin:0 0 12px;color:#991b1b;">Invoice {{Invoice_No}} overdue since {{Due_Date}}. Booking may go On Hold.</div>'
        + _grid(
            [
                ("Customer", "Customer_Name"),
                ("Amount", "Due_Amount"),
                ("RM", "RM_Name"),
                ("Destination", "Destination"),
            ]
        )
        + "<p><strong>RM action:</strong> Follow up with customer today.<br><strong>Account:</strong> Hold supplier bookings until cleared.</p>",
        whatsapp_text="""🔴 *Payment Overdue*

{{Customer_ID}} · {{Customer_Name}}
₹{{Due_Amount}} · Due {{Due_Date}}
✈️ {{Destination}}

RM {{RM_Name}} — please follow up.
Booking On Hold until paid.""",
    )
)

_register(
    NotificationTemplate(
        id="team_escalation",
        subject="[Escalation] Lead {{Temp_ID}} — RM not accepted · {{Elapsed_Time}}",
        email_subheader="Escalation · {{Escalation_Level}}",
        hero_title="",
        hero_subtitle="",
        email_body_html='<div style="background:#fef2f2;border:1px solid #fecaca;border-radius:6px;padding:12px;margin:0 0 12px;color:#991b1b;">{{Escalation_Message}}</div>'
        + _grid(
            [
                ("Lead", "Temp_ID"),
                ("Assigned RM", "RM_Name"),
                ("Customer", "Customer_Name"),
                ("Priority", "Priority"),
            ]
        )
        + '<div style="text-align:center;"><a href="{{CRM_Link}}" style="display:inline-block;background:#b91c1c;color:#fff;text-decoration:none;padding:10px 22px;border-radius:6px;font-weight:600;">Reassign Lead →</a></div>',
        whatsapp_text=None,
        wrap_layout=True,
    )
)


def get_template(template_id: str) -> NotificationTemplate:
    if template_id not in _TEMPLATES:
        raise KeyError(f"Unknown notification template: {template_id}")
    return _TEMPLATES[template_id]
