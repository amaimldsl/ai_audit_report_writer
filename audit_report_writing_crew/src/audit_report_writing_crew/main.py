#!/usr/bin/env python
import sys
import warnings

from crew import AuditReportWritingCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """

    #finding_condition = input("What is the audit finding condition? ")
    #finding_criteria = input("What is the audit finding criteria? ")    
    #finding_rca = input("What is the audit finding root cause analysis? ")
    #finding_risk = input("What is the audit finding risk? ")
    #finding_management_action = input("What is the audit finding management action? ")

    finding_condition = "The audit identified that 15 procurement contracts, valued at over $2 million, were awarded without obtaining the required competitive bids. These contracts were directly negotiated with vendors without documenting any justification for bypassing the bidding process."
    finding_criteria = "Company procurement policy mandates that contracts exceeding $100,000 must undergo a competitive bidding process to ensure fairness, cost-effectiveness, and compliance with internal controls. Any deviation from this process must be properly documented and approved by senior management."
    finding_rca = "The failure to follow the competitive bidding process was due to a lack of oversight in the procurement department. Staff responsible for contract approvals did not consistently enforce or monitor compliance with the bidding policy, and there was inadequate training on procurement procedures."
    finding_risk = "By bypassing the competitive bidding process, the company risks overpaying for goods and services, potentially entering into unfavorable contracts. Additionally, non-compliance with procurement policies could expose the company to reputational risks, regulatory scrutiny, and potential legal challenges."
    finding_management_action = """" To address the identified issue: Enforce Procurement Policies,Improve Oversight and Monitoring,Training and Awareness,Document and Approve Exceptions and Strengthen Internal Controls.
            """
    inputs = {
        'finding_condition': finding_condition,
        'finding_criteria': finding_criteria,
        'finding_rca': finding_rca,
        'finding_risk': finding_risk,
        'finding_management_action': finding_management_action
    }
    AuditReportWritingCrew().crew().kickoff(inputs=inputs)


run()