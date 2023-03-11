import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class CertificateHolder:
    '''Represents a holder of **X509Certificate2** instance.
    To learn more, visit the `Work with Digital Signatures <https://docs.aspose.com/words/net/working-with-digital-signatures/>` documentation article.
    
    :class:`CertificateHolder` can be created by static factory methods only.
    It contains an instance of **X509Certificate2** which is used to introduce private, public keys and certificate chains into the system.
    This class is applied in :class:`DigitalSignatureUtil` and :class:`aspose.words.saving.PdfDigitalSignatureDetails` instead of obsolete methods with
    System.Security.Cryptography.X509Certificates.X509Certificate2 as parameters.'''
    
    @overload
    @staticmethod
    def create(self, cert_bytes: bytes, password: str) -> aspose.words.digitalsignatures.CertificateHolder:
        '''Creates :class:`CertificateHolder` object using byte array of PKCS12 store and its password.
        
        :param cert_bytes: A byte array that contains data from an X.509 certificate.
        :param password: The password required to access the X.509 certificate data.
        :returns: An instance of :class:`CertificateHolder`
        
        :raises Org.BouncyCastle.Security.InvalidParameterException: Thrown if  is``None``
        :raises Org.BouncyCastle.Security.InvalidParameterException: Thrown if  is``None``
        :raises System.Security.SecurityException: Thrown if PKCS12 store contains no aliases
        :raises System.IO.IOException: Thrown if there is wrong password or corrupted file.'''
        ...
    
    @overload
    @staticmethod
    def create(self, file_name: str, password: str) -> aspose.words.digitalsignatures.CertificateHolder:
        '''Creates :class:`CertificateHolder` object using path to PKCS12 store and its password.
        
        :param file_name: The name of a certificate file.
        :param password: The password required to access the X.509 certificate data.
        :returns: An instance of :class:`CertificateHolder`
        
        :raises Org.BouncyCastle.Security.InvalidParameterException: Thrown if  is``None``
        :raises Org.BouncyCastle.Security.InvalidParameterException: Thrown if  is``None``
        :raises System.Security.SecurityException: Thrown if PKCS12 store contains no aliases
        :raises System.IO.IOException: Thrown if there is wrong password or corrupted file.'''
        ...
    
    @overload
    @staticmethod
    def create(self, file_name: str, password: str, alias: str) -> aspose.words.digitalsignatures.CertificateHolder:
        '''Creates :class:`CertificateHolder` object using path to PKCS12 store, its password and the alias by using which private key and certificate will be found.
        
        :param file_name: The name of a certificate file.
        :param password: The password required to access the X.509 certificate data.
        :param alias: The associated alias for a certificate and its private key
        :returns: An instance of :class:`CertificateHolder`
        
        :raises Org.BouncyCastle.Security.InvalidParameterException: Thrown if  is``None``
        :raises Org.BouncyCastle.Security.InvalidParameterException: Thrown if  is``None``
        :raises System.Security.SecurityException: Thrown if PKCS12 store contains no aliases
        :raises System.IO.IOException: Thrown if there is wrong password or corrupted file.
        :raises System.Security.SecurityException: Thrown if there is no private key with the given alias'''
        ...
    
    ...

class DigitalSignature:
    '''Represents a digital signature on a document and the result of its verification.
    To learn more, visit the `Work with Digital Signatures <https://docs.aspose.com/words/net/working-with-digital-signatures/>` documentation article.'''
    
    @property
    def signature_type(self) -> aspose.words.digitalsignatures.DigitalSignatureType:
        '''Gets the type of the digital signature.'''
        ...
    
    @property
    def sign_time(self) -> datetime.datetime:
        '''Gets the time the document was signed.'''
        ...
    
    @property
    def comments(self) -> str:
        '''Gets the signing purpose comment.'''
        ...
    
    @property
    def subject_name(self) -> str:
        '''Returns the subject distinguished name of the certificate that was used to sign the document.'''
        ...
    
    @property
    def issuer_name(self) -> str:
        '''Returns the subject distinguished name of the certificate isuuer.'''
        ...
    
    @property
    def is_valid(self) -> bool:
        '''Returns ``True`` if this digital signature is valid and the document has not been tampered with.'''
        ...
    
    @property
    def certificate_holder(self) -> aspose.words.digitalsignatures.CertificateHolder:
        '''Returns the certificate holder object that contains the certificate was used to sign the document.'''
        ...
    
    ...

class DigitalSignatureCollection:
    '''Provides a read-only collection of digital signatures attached to a document.
    To learn more, visit the `Work with Digital Signatures <https://docs.aspose.com/words/net/working-with-digital-signatures/>` documentation article.
    
    :attr:`aspose.words.Document.digital_signatures`'''
    
    def __init__(self):
        ...
    
    def __getitem__(self, index: int) -> aspose.words.digitalsignatures.DigitalSignature:
        '''Gets a document signature at the specified index.
        
        :param index: Zero-based index of the signature.'''
        ...
    
    @property
    def is_valid(self) -> bool:
        '''Returns ``True`` if all digital signatures in this collection are valid and the document has not been tampered with
        Also returns ``True`` if there are no digital signatures.
        Returns ``False`` if at least one digital signature is invalid.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of elements contained in the collection.'''
        ...
    
    ...

class DigitalSignatureUtil:
    '''Provides methods for signing document.
    To learn more, visit the `Work with Digital Signatures <https://docs.aspose.com/words/net/working-with-digital-signatures/>` documentation article.
    
    Since digital signature works with file content rather than Document Object Model these methods are put into a separate class.
    
    Supported formats are :attr:`aspose.words.LoadFormat.DOC` and :attr:`aspose.words.LoadFormat.DOCX`.'''
    
    @overload
    @staticmethod
    def sign(self, src_stream: io.BytesIO, dst_stream: io.BytesIO, cert_holder: aspose.words.digitalsignatures.CertificateHolder, sign_options: aspose.words.digitalsignatures.SignOptions) -> None:
        '''Signs source document using given :class:`CertificateHolder` and :class:`SignOptions`
        with digital signature and writes signed document to destination stream.
        Document should be either :attr:`aspose.words.LoadFormat.DOC` or :attr:`aspose.words.LoadFormat.DOCX`.
        
        **Output will be written to the start of stream and stream size will be updated with content length.**
        
        :param src_stream: The stream which contains the document to sign.
        :param dst_stream: The stream that signed document will be written to.
        :param cert_holder: :class:`CertificateHolder` object with certificate that used to sign file.
                            The certificate in holder MUST contain private keys and have the X509KeyStorageFlags.Exportable flag set.
        :param sign_options: :class:`SignOptions` object with various signing options.'''
        ...
    
    @overload
    @staticmethod
    def sign(self, src_file_name: str, dst_file_name: str, cert_holder: aspose.words.digitalsignatures.CertificateHolder, sign_options: aspose.words.digitalsignatures.SignOptions) -> None:
        '''Signs source document using given :class:`CertificateHolder` and :class:`SignOptions`
        with digital signature and writes signed document to destination file.
        Document should be either :attr:`aspose.words.LoadFormat.DOC` or :attr:`aspose.words.LoadFormat.DOCX`.
        
        :param src_file_name: The file name of the document to sign.
        :param dst_file_name: The file name of the signed document output.
        :param cert_holder: :class:`CertificateHolder` object with certificate that used to sign file.
                            The certificate in holder MUST contain private keys and have the X509KeyStorageFlags.Exportable flag set.
        :param sign_options: :class:`SignOptions` object with various signing options.'''
        ...
    
    @overload
    @staticmethod
    def sign(self, src_stream: io.BytesIO, dst_stream: io.BytesIO, cert_holder: aspose.words.digitalsignatures.CertificateHolder) -> None:
        '''Signs source document using given :class:`CertificateHolder` with digital signature
        and writes signed document to destination stream.
        Document should be either :attr:`aspose.words.LoadFormat.DOC` or :attr:`aspose.words.LoadFormat.DOCX`.
        
        **Output will be written to the start of stream and stream size will be updated with content length.**
        
        :param src_stream: The stream which contains the document to sign.
        :param dst_stream: The stream that signed document will be written to.
        :param cert_holder: :class:`CertificateHolder` object with certificate that used to sign file.
                            The certificate in holder MUST contain private keys and have the X509KeyStorageFlags.Exportable flag set.'''
        ...
    
    @overload
    @staticmethod
    def sign(self, src_file_name: str, dst_file_name: str, cert_holder: aspose.words.digitalsignatures.CertificateHolder) -> None:
        '''Signs source document using given :class:`CertificateHolder` with digital signature
        and writes signed document to destination file.
        Document should be either :attr:`aspose.words.LoadFormat.DOC` or :attr:`aspose.words.LoadFormat.DOCX`.
        
        :param src_file_name: The file name of the document to sign.
        :param dst_file_name: The file name of the signed document output.
        :param cert_holder: :class:`CertificateHolder` object with certificate that used to sign file.
                            The certificate in holder MUST contain private keys and have the X509KeyStorageFlags.Exportable flag set.'''
        ...
    
    @overload
    @staticmethod
    def remove_all_signatures(self, src_file_name: str, dst_file_name: str) -> None:
        '''Removes all digital signatures from source file and writes unsigned file to destination file.'''
        ...
    
    @overload
    @staticmethod
    def remove_all_signatures(self, src_stream: io.BytesIO, dst_stream: io.BytesIO) -> None:
        '''Removes all digital signatures from document in source stream and writes unsigned document to destination stream.
        **Output will be written to the start of stream and stream size will be updated with content length.**'''
        ...
    
    @overload
    @staticmethod
    def load_signatures(self, file_name: str) -> aspose.words.digitalsignatures.DigitalSignatureCollection:
        '''Loads digital signatures from document.
        
        :param file_name: Path to the document.
        :returns: Collection of digital signatures. Returns empty collection if file is not signed.'''
        ...
    
    @overload
    @staticmethod
    def load_signatures(self, stream: io.BytesIO) -> aspose.words.digitalsignatures.DigitalSignatureCollection:
        '''Loads digital signatures from document using stream.
        
        :param stream: Stream with the document.
        :returns: Collection of digital signatures. Returns empty collection if file is not signed.'''
        ...
    
    ...

class SignOptions:
    '''Allows to specify options for document signing.
    To learn more, visit the `Work with Digital Signatures <https://docs.aspose.com/words/net/working-with-digital-signatures/>` documentation article.'''
    
    def __init__(self):
        ...
    
    @property
    def comments(self) -> str:
        '''Specifies comments on the digital signature.
        Default value is **empty string** (System.String.Empty).'''
        ...
    
    @comments.setter
    def comments(self, value: str):
        ...
    
    @property
    def sign_time(self) -> datetime.datetime:
        '''The date of signing.
        Default value is **current time** (System.DateTime.Now).'''
        ...
    
    @sign_time.setter
    def sign_time(self, value: datetime.datetime):
        ...
    
    @property
    def signature_line_id(self) -> uuid.UUID:
        '''Signature line identifier.
        Default value is **Empty (all zeroes) Guid**.
        
        When set, it associates :class:`aspose.words.drawing.SignatureLine` with corresponding :class:`DigitalSignature`.'''
        ...
    
    @signature_line_id.setter
    def signature_line_id(self, value: uuid.UUID):
        ...
    
    @property
    def signature_line_image(self) -> bytes:
        '''The image that will be shown in associated :class:`aspose.words.drawing.SignatureLine`.
        Default value is ``None``.'''
        ...
    
    @signature_line_image.setter
    def signature_line_image(self, value: bytes):
        ...
    
    @property
    def decryption_password(self) -> str:
        '''The password to decrypt source document.
        Default value is **empty string** (System.String.Empty).
        
        If OOXML document is encrypted, you should provide decryption password
        to decrypt source document before it will be signed.
        This is not required for documents in binary DOC format.'''
        ...
    
    @decryption_password.setter
    def decryption_password(self, value: str):
        ...
    
    @property
    def provider_id(self) -> uuid.UUID:
        '''Specifies the class ID of the signature provider.
        Default value is **Empty (all zeroes) Guid**.
        
        The cryptographic service provider (CSP) is an independent software module that actually performs
        cryptography algorithms for authentication, encoding, and encryption. MS Office reserves the value
        of {00000000-0000-0000-0000-000000000000} for its default signature provider.
        
        The GUID of the additionally installed provider should be obtained from the documentation shipped with the provider.
        
        In addition, all the installed cryptographic providers are enumerated in windows registry.
        It can be found in the following path: HKLM\\SOFTWARE\\Microsoft\\Cryptography\\Defaults\\Provider.
        There is a key name "CP Service UUID" which corresponds to a GUID of signature provider.'''
        ...
    
    @provider_id.setter
    def provider_id(self, value: uuid.UUID):
        ...
    
    ...

class DigitalSignatureType:
    '''Specifies the type of a digital signature.'''
    
    UNKNOWN: int
    CRYPTO_API: int
    XML_DSIG: int

