from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterator, MutableSequence
from pydicom import config as config
from pydicom.charset import convert_encodings as convert_encodings, default_encoding as default_encoding
from pydicom.config import logger as logger
from pydicom.dataelem import DataElement as DataElement, DataElement_from_raw as DataElement_from_raw, RawDataElement as RawDataElement, empty_value_for_VR as empty_value_for_VR
from pydicom.dataset import Dataset as Dataset, FileDataset as FileDataset, FileMetaDataset as FileMetaDataset
from pydicom.errors import InvalidDicomError as InvalidDicomError
from pydicom.filebase import ReadableBuffer as ReadableBuffer
from pydicom.fileutil import PathType as PathType, path_from_pathlike as path_from_pathlike, read_undefined_length_value as read_undefined_length_value
from pydicom.misc import size_in_bytes as size_in_bytes, warn_and_log as warn_and_log
from pydicom.sequence import Sequence as Sequence
from pydicom.tag import BaseTag as BaseTag, ItemTag as ItemTag, SequenceDelimiterTag as SequenceDelimiterTag, Tag as Tag, TagListType as TagListType
from pydicom.util.hexutil import bytes2hex as bytes2hex
from pydicom.valuerep import EXPLICIT_VR_LENGTH_32 as EXPLICIT_VR_LENGTH_32
from typing import Any, BinaryIO

ENCODED_VR: Incomplete

def data_element_generator(fp: BinaryIO, is_implicit_VR: bool, is_little_endian: bool, stop_when: Callable[[BaseTag, str | None, int], bool] | None = None, defer_size: int | str | float | None = None, encoding: str | MutableSequence[str] = ..., specific_tags: list[BaseTag | int] | None = None) -> Iterator[RawDataElement | DataElement]: ...
def read_dataset(fp: BinaryIO, is_implicit_VR: bool, is_little_endian: bool, bytelength: int | None = None, stop_when: Callable[[BaseTag, str | None, int], bool] | None = None, defer_size: str | int | float | None = None, parent_encoding: str | MutableSequence[str] = ..., specific_tags: list[BaseTag | int] | None = None, at_top_level: bool = True) -> Dataset: ...
def read_sequence(fp: BinaryIO, is_implicit_VR: bool, is_little_endian: bool, bytelength: int, encoding: str | MutableSequence[str], offset: int = 0) -> Sequence: ...
def read_sequence_item(fp: BinaryIO, is_implicit_VR: bool, is_little_endian: bool, encoding: str | MutableSequence[str], offset: int = 0) -> Dataset | None: ...
def read_file_meta_info(filename: PathType) -> FileMetaDataset: ...
def read_preamble(fp: BinaryIO, force: bool) -> bytes | None: ...
def read_partial(fileobj: BinaryIO, stop_when: Callable[[BaseTag, str | None, int], bool] | None = None, defer_size: int | str | float | None = None, force: bool = False, specific_tags: list[BaseTag | int] | None = None) -> FileDataset: ...
def dcmread(fp: PathType | BinaryIO | ReadableBuffer, defer_size: str | int | float | None = None, stop_before_pixels: bool = False, force: bool = False, specific_tags: TagListType | None = None) -> FileDataset: ...
def data_element_offset_to_value(is_implicit_VR: bool, VR: str | None) -> int: ...
def read_deferred_data_element(fileobj_type: Any, filename_or_obj: PathType | BinaryIO, timestamp: float | None, raw_data_elem: RawDataElement) -> RawDataElement: ...
