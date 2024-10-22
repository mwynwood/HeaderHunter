import sys

def get_file_type(file_path):
    # Define magic numbers for common file types
    magic_numbers = {
        # Image formats
        b'\x89PNG\r\n\x1a\n': 'PNG image',
        b'GIF8': 'GIF image',
        b'\xff\xd8\xff': 'JPEG image',
        b'BM': 'BMP image',
        b'\x00\x00\x01\x00': 'ICO image',
        b'\x48\x49\x46\x38': 'HEIF image',
        b'\x00\x00\x00\x20ftyp': 'MP4 video (header)',
        b'Exif': 'Exif metadata',
        b'\xFF\xD8\xFF\xE0': 'JPEG image (Exif)',
    
        # Audio formats
        b'\xFF\xFB': 'MP3 audio',
        b'ID3': 'MP3 audio (ID3 tag)',
        b'OggS': 'Ogg container',
        b'WAVE': 'WAV audio',
        b'\x52\x49\x46\x46': 'WAV audio (RIFF)',
        b'\x1F\x8B': 'GZIP file',
        b'FLAC': 'FLAC audio',
        b'\x4D\x54\x68\x64': 'MIDI file',
    
        # Video formats
        b'RIFF': 'AVI file',
        b'\x1A\x45\xDF\xA3': 'Matroska (MKV) file',
        b'ftyp': 'MP4 file',
        b'\x00\x00\x00\x20ftyp': 'MP4 file (header)',
        b'cwebp': 'WebP image/video',
        b'6.0': 'QuickTime file',
        b'vids': 'AVI file',
        b'\x66\x74\x79\x70': 'MP4 file (ftyp)',
    
        # Document formats
        b'%PDF': 'PDF document',
        b'PK\x03\x04': 'ZIP archive',
        b'DOC': 'Word document (older)',
        b'\xD0\xCF\x11\xE0': 'Microsoft Office file (OLE)',
        b'PK\x05\x06': 'ZIP file (end of central directory)',
        b'<!DOCTYPE html': 'HTML document',
        b'<?xml': 'XML document',
    
        # Executable formats
        b'MZ': 'Windows executable (PE)',
        b'\x7FELF': 'ELF executable (Linux)',
        b'\x1F\x8B': 'GZIP file',
    
        # Archive formats
        b'Rar!': 'RAR archive',
        b'7z\xBC\xAF\x27\x1C': '7-Zip archive',
    
        # Misc formats
        b'FWS': 'SWF (Flash) file',
        b'\x00\x00\x00\x20': 'MP4 video',
        b'ANIM': 'Animation file',
        b'\x40\x43\x00\x00': 'CorelDRAW file',
        b'\x0E\x00\x00\x00': 'NetCDF file',
        b'\x7B\x5C\x72\x6F\x6F\x74': 'RoboHelp file',
    
        # Additional formats
        b'\x30\x26\xB2\x75\x8E\x66\xCF\x11': 'Microsoft Video file',
        b'\x00\x00\x00\x20': 'MP4 video',
        b'WMTv': 'Windows Media file',
        b'FLV': 'Flash Video file',
    }

    # Read the first 8 bytes of the file
    try:
        with open(file_path, 'rb') as f:
            header = f.read(8)
    except FileNotFoundError:
        return 'File not found.'
    except Exception as e:
        return f'Error reading file: {e}'

    # Check the header against known magic numbers
    for magic, file_type in magic_numbers.items():
        if header.startswith(magic):
            return file_type

    return 'Unknown file type'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python HeaderHunter.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_type = get_file_type(file_path)
    print(f'The file type is: {file_type}')
