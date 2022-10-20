from cgitb import text
from re import M
import tkinter
from tkinter import IntVar
from turtle import color
import pyperclip

# Set common notes
quick_notes = {
    "due date": " Mbr asked if they can change their due date. Agent informed the mbr that they can, and advised them on the process.",
    "payment": " Mbr wanted to make a payment. Agent scheduled the payment at their request.",
    "signing interest": " Mbr wanted to know why the interest rate on their signing docs is different than the one they saw in the application protal. Agent informed the mbr that the difference is because the rate on the signing docs doesn't include discounts.",
    "refinance": " Mbr wanted to know what options they have for a refinance. Agent advised the mbr of their options and described the refinance process.",
    "missing info": " Mbr asked what documentation is needed. Agent informed the mbr of what they need to upload",
    "intellicheck success": "Mbr wanted to change ___ on their profile. Agent walked the mbr through the intellicheck process and updated the profile\n\nContact number: \nIntellicheck was successful\nUploaded snip to documents\n",
    "log in help": "Mbr had forgotten their password and were unable to log onto their profile. Agent helped the mbr to reset their password.",
    "app questions": "Mbr wanted to know about our personal loan product and the process to apply. Agent answered general quesitons about the product and walked the mbr through the app process",
}

chat_quick_notes = {
    "due date reason": " Mbr asked if they can change their due date.",
    "due date action":  "Agent informed the mbr that they can, and advised them on the process.",
    "signing interest reason": " Mbr wanted to know why the interest rate on their signing docs is different than the one they saw in the application protal.",
    "signing interest action": "Agent informed the mbr that the difference is because the rate on the signing docs doesn't include discounts.",
    "refinance reason": "Mbr wanted to know what options they have for a refinance.",
    "refinance action": "Agent advised the mbr of their options and described the refinance process.",
    "missing info reason": "Mbr asked what documentation is needed.",
    "missing info action": "Agent informed the mbr of what they need to upload",
    "app questions reason": "Mbr wanted to know about our personal loan product and the process to apply.",
    "app questions action": "Agent answered general quesitons about the product and walked the mbr through the app process"
}

def note_select():
    window = tkinter.Tk()
    window.title("Sofee Note Generator")
    window.config(padx = 20, pady = 20)

    canvas = tkinter.Canvas(height = 200, width = 200)
    logo = tkinter.PhotoImage(file = "notes_app/download.png")
    canvas.create_image(100, 100, image = logo)
    canvas.pack()

    def phone_select():
        window.destroy()
        call_note()
    def chat_select():
        window.destroy()
        chat_note()

    phone_button = tkinter.Button(text="Inbound Call Notes", width=20, command=phone_select)
    phone_button.pack()

    chat_button = tkinter.Button(text="Chat Notes", width=20, command=chat_select)
    chat_button.pack()

    window.mainloop()

def call_note():
    # Window set up
    window = tkinter.Tk()
    window.title("Sofee Note Generator")
    window.config(padx = 20, pady = 20)

    # Create background image
    canvas = tkinter.Canvas(height = 200, width = 200)
    logo = tkinter.PhotoImage(file = "notes_app/download.png")
    canvas.create_image(100, 100, image = logo)
    canvas.grid(row = 0, column = 1)

    # Create the labels
    uid_label = tkinter.Label(text = "UID(Optional): ")
    uid_label.grid(row = 1, column = 0)

    Caller_id_label = tkinter.Label(text = "Caller ID: ")
    Caller_id_label.grid(row = 2, column = 0)

    Contact_id_label = tkinter.Label(text = "Contact ID: ")
    Contact_id_label.grid(row = 3, column = 0)

    notes_label = tkinter.Label(text = "Notes: ")
    notes_label.grid(row = 4, column = 0)

    # Create user input boxes
    text_inputs = []

    uid_input = tkinter.Text(height = 1, width = 21)
    uid_input.grid(row = 1, column = 1)
    text_inputs.append(uid_input)

    caller_id_input = tkinter.Text(height = 1, width = 21)
    caller_id_input.grid(row = 2, column = 1)
    text_inputs.append(caller_id_input)

    contact_id_input = tkinter.Text(height = 1, width = 21)
    contact_id_input.grid(row = 3, column = 1)
    text_inputs.append(contact_id_input)

    notes_input = tkinter.Text(height = 6, width = 60)
    notes_input.grid(row = 4, column = 1)
    text_inputs.append(notes_input)

    # Retreive inputed data
    def collect_data():
        uid = uid_input.get(1.0, 'end-1c')
        caller_id = caller_id_input.get(1.0, 'end-1c')
        contact_id = contact_id_input.get(1.0, 'end-1c')
        verification = is_verified()
        primary = is_primary()
        
        notes = notes_input.get(1.0, 'end-1c')

        call_note = f'Caller ID: {caller_id}\nContact ID: {contact_id}\nPrimary/Authorized (P/A): {primary}\nVerified (Y/N)?: {verification}\nGlance ID: \nNote: {notes}'
        pyperclip.copy(call_note)\
        
        for input in text_inputs:
            input.delete("1.0", "end")

        primary_checkbox.deselect()
        verified_checkbox.deselect()


    def is_primary():
        if primary_variable.get() == 1:
            return 'P'
        else:
            return 'A'

    def is_verified():
        if verified_variable.get() == 3:
            return 'Y'
        else:
            return 'N'

    primary_variable = IntVar()
    primary_checkbox = tkinter.Checkbutton(window, text='Primary?', variable = primary_variable, offvalue = 0, onvalue = 1, command = is_primary)
    primary_checkbox.grid(row = 9, column = 1)

    verified_variable = IntVar()
    verified_checkbox = tkinter.Checkbutton(window, text='Verified?', variable = verified_variable, offvalue = 2, onvalue = 3, command = is_verified)
    verified_checkbox.grid(row = 10, column = 1)

    # Create buttons
    def due_date_note():
        note = quick_notes["due date"]
        notes_input.insert('end', note)

    def payment_note():
        note = quick_notes["payment"]
        notes_input.insert('end', note)

    def signing_interest_note():
        note = quick_notes["signing interest"]
        notes_input.insert('end', note)

    def refinance_note():
        note = quick_notes["refinance"]
        notes_input.insert('end', note)

    def missing_info_note():
        note = quick_notes["due date"]
        notes_input.insert('end', note)
    
    def intellicheck_note():
        note = quick_notes["intellicheck success"]
        notes_input.insert('end', note)
    
    def log_in_help_note():
        note = quick_notes["log in help"]
        notes_input.insert('end', note)
    
    def  application_process_note():
        note = quick_notes["app questions"]
        notes_input.insert('end', note)

    due_date = tkinter.Button(text = "Due Date Change", command = due_date_note, width=18)
    due_date.grid(row = 11, column = 1)

    payment = tkinter.Button(text = "Payment", command = payment_note, width=18)
    payment.grid(row = 12, column = 1)

    signing_interest = tkinter.Button(text = "Signing Interest", command = signing_interest_note, width=18)
    signing_interest.grid(row = 13, column = 1)

    refinance = tkinter.Button(text = "Refinance", command = refinance_note, width = 18)
    refinance.grid(row = 14, column = 1)

    missing_info = tkinter.Button(text = "Missing info", command = missing_info_note, width = 18)
    missing_info.grid(row = 15, column = 1)

    intellicheck_success = tkinter.Button(text = "Intellicheck Success", command = intellicheck_note, width = 18)
    intellicheck_success.grid(row = 16, column = 1)

    log_in_help = tkinter.Button(text = "Log in Help", command = log_in_help_note, width = 18)
    log_in_help.grid(row = 17, column = 1)

    application_process= tkinter.Button(text = "Application Process", command = application_process_note, width = 18)
    application_process.grid(row = 18, column = 1)

    generate = tkinter.Button(text = "Generate", command = collect_data)
    generate.grid(row = 19, column = 1)

    window.mainloop()

def chat_note():
    window = tkinter.Tk()
    window.title("Sofee Note Generator")
    window.config(padx = 20, pady = 20)

    canvas = tkinter.Canvas(height = 200, width = 200)
    logo = tkinter.PhotoImage(file = "notes_app/download.png")
    canvas.create_image(100, 100, image = logo)
    canvas.grid(row = 0, column = 1)

    # Create labels
    uid_label = tkinter.Label(text="UID(optional): ")
    uid_label.grid(row = 1, column = 0)

    ticket_label = tkinter.Label(text = "Ticket Number: ")
    ticket_label.grid(row = 2, column = 0)

    interaction_reason_label = tkinter.Label(text = "Reason for interaction: ")
    interaction_reason_label.grid(row = 3, column = 0)

    actions_taken_label = tkinter.Label(text = "Actions Taken: ")
    actions_taken_label.grid(row = 4, column = 0)

    # Create text entry boxes
    text_inputs = []

    uid_input = tkinter.Text(height = 1, width = 21)
    uid_input.grid(row = 1, column = 1)
    text_inputs.append(uid_input)

    ticket_input = tkinter.Text(height = 1, width = 21)
    ticket_input.grid(row = 2, column = 1)
    text_inputs.append(ticket_input)

    interaction_reason_input = tkinter.Text(height = 3, width = 60)
    interaction_reason_input.grid(row = 3, column = 1)
    text_inputs.append(interaction_reason_input)

    actions_taken_input = tkinter.Text(height = 3, width = 60)
    actions_taken_input.grid(row = 4, column = 1)
    text_inputs.append(actions_taken_input)

    # Create checkbox
    def is_complaint():
        if complaint_variable.get() == 1:
            return 'Y'
        else:
            return 'N'

    complaint_variable = IntVar()
    complaint_checkbox = tkinter.Checkbutton(window, text='Complaint?', variable = complaint_variable, offvalue = 0, onvalue = 1, command = is_complaint)
    complaint_checkbox.grid(row = 5, column = 1)

    # Create quick notes
    def due_date_note():
        reason = chat_quick_notes["due date reason"]
        action = chat_quick_notes["due date action"]
        interaction_reason_input.insert('end', reason)
        actions_taken_input.insert('end', action)

    def signing_interest_note():
        reason = chat_quick_notes["signing interest reason"]
        action = chat_quick_notes["signing interest action"]
        interaction_reason_input.insert('end', reason)
        actions_taken_input.insert('end', action)
    
    def refinance_note():
        reason = chat_quick_notes["refinance reason"]
        action = chat_quick_notes["refinance action"]
        interaction_reason_input.insert('end', reason)
        actions_taken_input.insert('end', action)
    
    def missing_info_note():
        reason = chat_quick_notes["missing info reason"]
        action = chat_quick_notes["missing info action"]
        interaction_reason_input.insert('end', reason)
        actions_taken_input.insert('end', action)
    
    def application_questions_note():
        reason = chat_quick_notes["app questions reason"]
        action = chat_quick_notes["app questions action"]
        interaction_reason_input.insert('end', reason)
        actions_taken_input.insert('end', action)

    due_date = tkinter.Button(text = "Due Date Change", command = due_date_note, width=18)
    due_date.grid(row = 6, column = 1)

    signing_interest = tkinter.Button(text = "Signing Interest", command = signing_interest_note, width=18)
    signing_interest.grid(row = 7, column = 1)

    refinance = tkinter.Button(text = "Refinance", command = refinance_note, width=18)
    refinance.grid(row = 8, column = 1)

    missing_info = tkinter.Button(text = "Missing Info", command = missing_info_note, width=18)
    missing_info.grid(row = 9, column = 1)

    application_questions = tkinter.Button(text = "Application Process", command = application_questions_note, width=18)
    application_questions.grid(row = 10, column = 1)

    def collect_data():
            uid = uid_input.get(1.0, 'end-1c')
            ticket = ticket_input.get(1.0, 'end-1c')
            reason_for_interaction = interaction_reason_input.get(1.0, 'end-1c')
            agent_actions = actions_taken_input.get(1.0, 'end-1c')
            complaint = is_complaint()

            call_note = f'Chat Ticket #: {ticket}\nReason for interaction: {reason_for_interaction}\nActions taken by agent: {agent_actions}\nComplaint (Y/N)?: {complaint}'
            pyperclip.copy(call_note)\
            
            for input in text_inputs:
                input.delete("1.0", "end")

            complaint_checkbox.deselect()

    generate = tkinter.Button(text = "Generate", command = collect_data)
    generate.grid(row = 11, column = 1)

    window.mainloop()

note_select()