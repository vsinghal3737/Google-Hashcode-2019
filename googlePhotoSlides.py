def googlePhotoSlides(inputFileName, outputFileName):
    DataStructure, Tagmapping = {}, {}
    lst = []
    with open(inputFileName, 'r') as jabber:
        i, ID = 0, 0
        for line in jabber:
            if i == 0:
                NumofPictures = line
                i += 1
            else:
                temp = line
                templist = temp[4:].split()
                DataStructure[ID] = [ID, [temp[0], temp[2], templist]]
                for i in templist:
                    if i not in Tagmapping.keys():
                        Tagmapping[i] = [ID]
                    else:
                        minitemp = Tagmapping[i]
                        minitemp.append(ID)
                        Tagmapping[i] = minitemp
                lst.append(ID)
                ID += 1

    # print(DataStructure)
    # print()
    # print()

    # for i in DataStructure:
    #     print(DataStructure[i])

    output, temp = [], []
    for i in Tagmapping:
        EveryID_in_one_Tag = Tagmapping[i]
        while len(EveryID_in_one_Tag) > 0:
            if EveryID_in_one_Tag[0] in lst:
                if DataStructure[EveryID_in_one_Tag[0]][1][0] == "H":
                    output.append(EveryID_in_one_Tag[0])
                    lst.remove(EveryID_in_one_Tag[0])
                else:
                    if len(temp) == 0:
                        temp = [EveryID_in_one_Tag[0]]
                        lst.remove(EveryID_in_one_Tag[0])
                    else:
                        temp.append(EveryID_in_one_Tag[0])
                        lst.remove(EveryID_in_one_Tag[0])
                        temp = str(temp[0]) + " " + str(temp[1])
                        output.append(temp)
                        temp = []
            del EveryID_in_one_Tag[0]

    with open(outputFileName, 'w') as filehandle:
        print(len(output), file=filehandle)
        filehandle.writelines("%s\n" % lines for lines in output)


# googlePhotoSlides("InputDataSets\\a_example.txt", "Output\\a_output.txt")
# googlePhotoSlides("InputDataSets\\b_lovely_landscapes.txt", "Output\\b_output.txt")
# googlePhotoSlides("InputDataSets\\c_memorable_moments.txt", "Output\\c_output.txt")
# googlePhotoSlides("InputDataSets\\d_pet_pictures.txt", "Output\\d_output.txt")
# googlePhotoSlides("InputDataSets\\e_shiny_selfies.txt", "Output\\e_output.txt")
