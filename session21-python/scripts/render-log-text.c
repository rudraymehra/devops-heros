/* Offline text-to-PNG helper for macOS. No browser, display capture or network. */
#include <CoreFoundation/CoreFoundation.h>
#include <CoreGraphics/CoreGraphics.h>
#include <CoreText/CoreText.h>
#include <ImageIO/ImageIO.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
    if (argc != 3) { fprintf(stderr, "usage: render-log-text input.txt output.png\n"); return 2; }
    FILE *input = fopen(argv[1], "r");
    if (!input) { perror("input"); return 1; }
    char *line = NULL;
    size_t capacity = 0, count = 0;
    while (getline(&line, &capacity, input) >= 0) count++;
    rewind(input);
    const size_t width = 1840, height = 80 + count * 26;
    CGColorSpaceRef colors = CGColorSpaceCreateDeviceRGB();
    CGContextRef context = CGBitmapContextCreate(NULL, width, height, 8, width * 4,
        colors, kCGImageAlphaPremultipliedLast);
    if (!context) { fclose(input); free(line); CGColorSpaceRelease(colors); return 1; }
    CGContextSetRGBFillColor(context, 0.97, 0.98, 0.99, 1);
    CGContextFillRect(context, CGRectMake(0, 0, width, height));
    CGContextSetRGBFillColor(context, 1, 0.92, 0.72, 1);
    CGContextFillRect(context, CGRectMake(20, height - 66, width - 40, 44));
    CTFontRef font = CTFontCreateWithName(CFSTR("Menlo"), 16, NULL);
    CGColorRef ink = CGColorCreateGenericRGB(0.08, 0.12, 0.18, 1);
    const void *keys[] = {kCTFontAttributeName, kCTForegroundColorAttributeName};
    const void *values[] = {font, ink};
    CFDictionaryRef attributes = CFDictionaryCreate(NULL, keys, values, 2,
        &kCFTypeDictionaryKeyCallBacks, &kCFTypeDictionaryValueCallBacks);
    size_t number = 0;
    while (getline(&line, &capacity, input) >= 0) {
        line[strcspn(line, "\r\n")] = 0;
        CFStringRef text = CFStringCreateWithCString(NULL, line, kCFStringEncodingUTF8);
        if (!text) { fprintf(stderr, "Invalid UTF-8 on line %zu\n", number + 1); return 1; }
        CFAttributedStringRef attributed = CFAttributedStringCreate(NULL, text, attributes);
        CTLineRef shaped = CTLineCreateWithAttributedString(attributed);
        CGContextSetTextPosition(context, 36, height - 50 - number * 26);
        CTLineDraw(shaped, context);
        CFRelease(shaped); CFRelease(attributed); CFRelease(text);
        number++;
    }
    fclose(input); free(line);
    CGImageRef image = CGBitmapContextCreateImage(context);
    CFURLRef destination = CFURLCreateFromFileSystemRepresentation(NULL,
        (const UInt8 *)argv[2], strlen(argv[2]), false);
    CGImageDestinationRef writer = CGImageDestinationCreateWithURL(destination, CFSTR("public.png"), 1, NULL);
    if (!writer || !image) { fprintf(stderr, "Cannot create PNG\n"); return 1; }
    CGImageDestinationAddImage(writer, image, NULL);
    bool ok = CGImageDestinationFinalize(writer);
    CFRelease(writer); CFRelease(destination); CGImageRelease(image);
    CFRelease(attributes); CGColorRelease(ink); CFRelease(font);
    CGContextRelease(context); CGColorSpaceRelease(colors);
    return ok ? 0 : 1;
}
