import os
import numpy as np

from pathlib import Path

BASE_FOLDER = Path(os.path.abspath(os.path.curdir))
DATA_FOLDER = BASE_FOLDER / "data"

from typing import Sequence

# from collections import namedtuple
from dataclasses import dataclass


@dataclass
class Patient:
    pid: str
    sex: str
    group: str
    age: int
    inf_data: Sequence[int]

    def stratification_label(self) -> str:
        """
        Return the group label of a Patient obtained
        by concatenation of sex and group.
        """
        return f"{self.sex}-{self.group}"


# Patient = namedtuple("Patient", ["pid", "sex", "group", "age", "inf_data"])
# Dataset = Sequence[Patient]


class Dataset:
    def __init__(self, patients: Sequence[Patient]):
        self.patients = patients

    def __len__(self):
        return len(self.patients)

    def __getitem__(self, index) -> Patient:
        return self.patients[index]


# expect reading inflammation-04.csv format
def read_inflammation_data(filename: str) -> Dataset:
    """
    Read dataset in ver4 format.

    Parameters
    ----------
    filename : str
        Name of the datafile to use in input.
        The file is assumed to be located in DATA_FOLDER

    Raises
    ------
        ValueError
            When input filename does not correspond to
            any file in DATA FOLDER

    Returns
    -------
    Dataset
        Sequence of `Patient` tuple
    """

    datafilepath = DATA_FOLDER / filename
    if not datafilepath.exists():
        raise ValueError(
            f"Input filename {filename} has not been found in Data Folder!"
        )
    with open(datafilepath) as datafile:
        patients_list = list()
        for i, line in enumerate(datafile):
            if i == 0:
                continue
            line = line.strip()
            pinfo = line.split(",")
            patient = Patient(
                pid=pinfo[0],
                group=pinfo[-1],
                age=int(pinfo[-2]),
                sex=pinfo[-3],
                inf_data=np.asarray(pinfo[1:-3]).astype(int),
            )
            patients_list.append(patient)
        dataset = Dataset(patients=patients_list)
        return dataset
