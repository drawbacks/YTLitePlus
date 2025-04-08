#!/usr/bin/env python3

def main():
	file_path = "Tweaks/YTLite/var/jb/Library/MobileSubstrate/DynamicLibraries/YTLite.dylib"
	replacements = [
		("YTLitePlus.dylib", "YTLitePlus.dylip"),
		("uYou.dylib", "uYou.dylip"),
		("uYouPlus.dylib", "uYouPlus.dylip"),
		("iSponsorBlock.dylib", "iSponsorBlock.dylip"),
		("DLTube.dylib", "DLTube.dylip"),
		("DLYouTube.dylib", "DLYouTube.dylip"),
		("YouTubeReborn.dylib", "YouTubeReborn.dylip"),
		("uYouEnhanced.dylib", "uYouEnhanced.dylip"),
		("YouTimeStamp.dylib", "YouTimeStamp.dylip"),
		("YTRebornObjc.dylib", "YTRebornObjc.dylip")
	]
	with open(file_path, "rb+") as file:
		content = file.read()

		for target, replacement in replacements:
			print("[*] Replacing", target, "with", replacement)
			
			target_bytes = target.encode("utf-8")
			replacement_bytes = replacement.encode("utf-8")
			content = content.replace(target_bytes, replacement_bytes)
		
		file.seek(0)        
		file.write(content)
		file.truncate()
		file.close()
		
	print("[*] Done replacing dylibs in YTLite.dylib!")

if __name__ == "__main__":
	main()
