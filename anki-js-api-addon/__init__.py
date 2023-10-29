from typing import Any, Tuple

import aqt
from aqt import gui_hooks, mw
from anki.scheduler.v3 import Scheduler as V3Scheduler

command_prefix = "AnkiJS."

def on_webview_did_receive_js_message(
    handled: Tuple[bool, Any], message: str, context: Any
):
    # Run only on the reviewer's webview
    if not isinstance(context, aqt.reviewer.Reviewer):
        return handled

    if message.startswith(command_prefix):
        ret = None
        try:
            new, lrn, rev = mw.col.sched.counts(mw.reviewer.card)
            cmd = message[len(command_prefix) :].strip()
            ret = None
            if cmd == "ankiGetNewCardCount()":
                ret = new

            elif cmd == "ankiGetLrnCardCount()":
                ret = lrn

            elif cmd == "ankiGetRevCardCount()":
                ret = rev

            elif cmd == "ankiGetCardMark()":
                ret = mw.reviewer.card.note().hasTag("marked")

            elif cmd == "ankiGetCardFlag()":
                ret = mw.reviewer.card.userFlag()

            elif cmd == "ankiGetCardId()":
                ret = mw.reviewer.card.id

            elif cmd == "ankiGetCardNid()":
                ret = mw.reviewer.card.nid

            elif cmd == "ankiGetCardDid()":
                ret = mw.reviewer.card.did

            elif cmd == "ankiGetCardMod()":
                ret = mw.reviewer.card.mod

            elif cmd == "ankiGetCardType()":
                ret = mw.reviewer.card.type

            elif cmd == "ankiGetCardQueue()":
                ret = mw.reviewer.card.queue

            elif cmd == "ankiGetCardLeft()":
                ret = mw.reviewer.card.left

            elif cmd == "ankiGetCardDue()":
                ret = mw.reviewer.card.due

            elif cmd == "ankiGetCardInterval()":
                ret = mw.reviewer.card.ivl

            elif cmd == "ankiGetCardFactor()":
                ret = mw.reviewer.card.factor

            elif cmd == "ankiGetCardReps()":
                ret = mw.reviewer.card.reps

            elif cmd == "ankiGetCardLapses()":
                ret = mw.reviewer.card.lapses

            elif cmd == "ankiGetCardODue()":
                ret = mw.reviewer.card.odue

            elif cmd == "ankiGetCardODid()":
                ret = mw.reviewer.card.odid

            elif cmd == "ankiGetNextTime1()" or cmd == "ankiGetNextTime2()" or cmd == "ankiGetNextTime3()" or cmd == "ankiGetNextTime4()":
                i = int(cmd[len("ankiGetNextTime") :][0])
                if v3 := context._v3:
                    assert isinstance(mw.col.sched, V3Scheduler)
                    labels = mw.col.sched.describe_next_states(v3.states)
                    ret = labels[i - 1]
                else:
                    ret = mw.col.sched.nextIvlStr(mw.reviewer.card, i, True) or "&nbsp;"
                       

        except Exception as e:
            ret = repr(e)
        finally:
            return (True, ret)
    else:
        return handled

gui_hooks.webview_did_receive_js_message.append(on_webview_did_receive_js_message)
