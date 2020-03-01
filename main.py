from midiutil import MIDIFile
from Note import Note
import random

#This array holds the MIDI numbers for each of the pitches in a C Major Scale
CMajor = [Note.C1.value, Note.D1.value, Note.E1.value, Note.F1.value, Note.G1.value, Note.A1.value, Note.B1.value,
          Note.C2.value, Note.D2.value, Note.E2.value, Note.F2.value, Note.G2.value, Note.A2.value, Note.B2.value,
          Note.C3.value, Note.D3.value, Note.E3.value, Note.F3.value, Note.G3.value, Note.A3.value, Note.B3.value,
          Note.C4.value, Note.D4.value, Note.E4.value, Note.F4.value, Note.G4.value, Note.A4.value, Note.B4.value,
          Note.C5.value, Note.D5.value, Note.E5.value, Note.F5.value, Note.G5.value, Note.A5.value, Note.B5.value,
          Note.C6.value, Note.D6.value, Note.E6.value, Note.F6.value, Note.G6.value, Note.A6.value, Note.B6.value,
          Note.C7.value, Note.D7.value, Note.E7.value, Note.F7.value, Note.G7.value, Note.A7.value, Note.B7.value,
          Note.C8.value, Note.D8.value, Note.E8.value, Note.F8.value, Note.G8.value, Note.A8.value, Note.B8.value,
          Note.C9.value, Note.D9.value, Note.E9.value, Note.F9.value, Note.G9.value]


def createMIDI(tempo):

    midiFile = MIDIFile(1)

    midiFile.addTempo(0, 0, tempo)

    return midiFile


#Randomly picks 8 patterns that are each 1 beat long to create a "melody"
def createMelody():

    melody = []

    previousNote = 28 #The index in the CMajor array that corresponds to C5

    for i in range(8):

        pattern = random.randint(1,7)

        #The notes of the pattern will move upwards/downwards in either whole steps or thirds
        direction = random.choice([-1, 1])
        step = random.randint(1,2)
        direction = direction * step
        

        if pattern == 1:
            melody.append((CMajor[previousNote+direction],0.25))
            previousNote = previousNote+direction

            melody.append((CMajor[previousNote+direction],0.25))
            previousNote = previousNote+direction

            melody.append((CMajor[previousNote+direction],0.25))
            previousNote = previousNote+direction

            melody.append((CMajor[previousNote+direction],0.25))
            previousNote = previousNote+direction
            

        elif pattern == 2:
            melody.append((CMajor[previousNote+direction],0.5))
            previousNote = previousNote+direction

            melody.append((CMajor[previousNote+direction],0.25))
            previousNote = previousNote+direction

            melody.append((CMajor[previousNote+direction],0.25))
            previousNote = previousNote+direction


        elif pattern == 3:
            melody.append((CMajor[previousNote+direction],0.25))
            previousNote = previousNote+direction

            melody.append((CMajor[previousNote+direction],0.25))
            previousNote = previousNote+direction

            melody.append((CMajor[previousNote+direction],0.5))
            previousNote = previousNote+direction


        elif pattern == 4:
            melody.append((CMajor[previousNote+direction],0.75))
            previousNote = previousNote+direction

            melody.append((CMajor[previousNote+direction],0.25))
            previousNote = previousNote+direction


        elif pattern == 5:
            melody.append((CMajor[previousNote+direction],0.25))
            previousNote = previousNote+direction

            melody.append((CMajor[previousNote+direction],0.5))
            previousNote = previousNote+direction

            melody.append((CMajor[previousNote+direction],0.25))
            previousNote = previousNote+direction


        elif pattern == 6:
            melody.append((CMajor[previousNote+direction],1))
            previousNote = previousNote+direction


        elif pattern == 7:
            melody.append((CMajor[previousNote+direction],0.5))
            previousNote = previousNote+direction

            melody.append((CMajor[previousNote+direction],0.5))
            previousNote = previousNote+direction

        
    return melody



def createOutput(midiFile, melody):

    totaltime = 0

    for i, (pitch, duration) in enumerate(melody):
        midiFile.addNote(0, 0, pitch, totaltime + i, duration, 100)
        totaltime+=(duration-1)
 

    with open("melody.mid", "wb") as output_file:
        midiFile.writeFile(output_file)


def main():

    midiFile = createMIDI(108)

    melody = createMelody()

    createOutput(midiFile, melody)



if __name__ == '__main__':
    main() 
