"""
Test script for complete certificate generation flow
Run with: python manage.py shell < test_complete_flow.py
"""

from .models import User
from cert_gen_sen_app_backend.models import Event, Participant, Template
from cert_gen_sen_app_backend.services.pdf_service import PDFService

print("=" * 60)
print("Testing Certificate Generation Flow")
print("=" * 60)

# 1. Get or create a user
user, created = User.objects.get_or_create(
    username="testuser", defaults={"email": "test@example.com"}
)
if created:
    user.set_password("testpass123")
    user.save()
print(f"✓ User: {user.username}")

# 2. Create a template
template_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            padding: 0;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .container {
            width: 800px;
            margin: 50px auto;
            background: white;
            padding: 50px;
            box-shadow: 0 10px 50px rgba(0,0,0,0.3);
        }
        .certificate {
            border: 15px solid #667eea;
            padding: 50px;
            text-align: center;
        }
        h1 {
            color: #667eea;
            font-size: 48px;
            margin: 20px 0;
            text-transform: uppercase;
            letter-spacing: 3px;
        }
        .recipient {
            font-size: 36px;
            color: #333;
            margin: 30px 0;
            font-weight: bold;
        }
        .event-name {
            font-size: 28px;
            color: #764ba2;
            margin: 20px 0;
        }
        .details {
            font-size: 18px;
            color: #666;
            margin: 10px 0;
        }
        .footer {
            margin-top: 50px;
            padding-top: 30px;
            border-top: 2px solid #667eea;
        }
        .signature {
            display: inline-block;
            width: 200px;
            margin: 0 30px;
        }
        .line {
            border-top: 2px solid #333;
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="certificate">
            <h1>Certificate of Achievement</h1>
            
            <p class="details">This is to certify that</p>
            
            <div class="recipient">{{ participant_name }}</div>
            
            <p class="details">has successfully completed</p>
            
            <div class="event-name">{{ event_name }}</div>
            
            <p class="details">
                held on {{ event_date }}<br>
                at {{ event_location }}
            </p>
            
            <div class="footer">
                <div class="signature">
                    <div class="line"></div>
                    <p>Instructor Signature</p>
                </div>
                <div class="signature">
                    <div class="line"></div>
                    <p>Director Signature</p>
                </div>
            </div>
            
            <p style="margin-top: 30px; font-size: 14px; color: #999;">
                Certificate ID: {{ participant_id }} | Email: {{ participant_email }}
            </p>
        </div>
    </div>
</body>
</html>
"""

template, created = Template.objects.get_or_create(
    user=user,
    template_name="Professional Certificate",
    defaults={"html_content": template_html},
)
if not created:
    template.html_content = template_html
    template.save()
print(f"✓ Template: {template.template_name} (ID: {template.id})")

# 3. Create an event
event, created = Event.objects.get_or_create(
    user=user,
    event="Python Workshop",
    defaults={
        "details": {
            "event_name": "Advanced Python Programming Workshop 2024",
            "event_date": "October 25, 2024",
            "event_location": "Tech Hub, San Francisco",
            "event_duration": "3 Days",
        }
    },
)
print(f"✓ Event: {event.event} (ID: {event.id})")

# 4. Create participants
participants_data = [
    {
        "participant_name": "Alice Johnson",
        "participant_email": "alice@example.com",
        "participant_id": "PY2024001",
    },
    {
        "participant_name": "Bob Smith",
        "participant_email": "bob@example.com",
        "participant_id": "PY2024002",
    },
    {
        "participant_name": "Carol Williams",
        "participant_email": "carol@example.com",
        "participant_id": "PY2024003",
    },
]

print("\n✓ Creating participants...")
for p_data in participants_data:
    participant, created = Participant.objects.get_or_create(
        event=event, participant_details=p_data
    )
    print(f"  - {p_data['participant_name']} (ID: {participant.id})")

# 5. Test PDF generation for one participant
print("\n" + "=" * 60)
print("Testing Single Certificate Generation")
print("=" * 60)

first_participant = event.participants.first()
if first_participant:
    print(
        f"Generating certificate for: {first_participant.participant_details['participant_name']}"
    )

    pdf_bytes, success, message = PDFService.generate_certificate(
        event, first_participant, template
    )

    if success:
        filename = f"certificate_{first_participant.id}.pdf"
        with open(filename, "wb") as f:
            f.write(pdf_bytes)
        print(f"✓ SUCCESS! Certificate saved: {filename}")
        print(f"  File size: {len(pdf_bytes)} bytes")
    else:
        print(f"✗ FAILED: {message}")

# 6. Test bulk generation
print("\n" + "=" * 60)
print("Testing Bulk Certificate Generation")
print("=" * 60)

results = PDFService.generate_bulk_certificates(event, template)

successful = [r for r in results if r[2]]
failed = [r for r in results if not r[2]]

print(f"\nTotal: {len(results)}")
print(f"Successful: {len(successful)}")
print(f"Failed: {len(failed)}")

for participant_id, pdf_bytes, success, message in results:
    participant = Participant.objects.get(id=participant_id)
    name = participant.participant_details["participant_name"]

    if success:
        filename = f"bulk_certificate_{participant_id}.pdf"
        with open(filename, "wb") as f:
            f.write(pdf_bytes)
        print(f"✓ {name}: {filename}")
    else:
        print(f"✗ {name}: {message}")

print("\n" + "=" * 60)
print("Test Complete!")
print("=" * 60)
print("\nNext steps:")
print("1. Check the generated PDF files in your current directory")
print("2. Start Django server: python manage.py runserver")
print("3. Test API endpoints with curl or Postman")
print("4. Access admin panel: http://localhost:8000/admin/")
