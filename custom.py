# custom.py
production = "yes"
debug_symbols="no"
optimize="speed_trace" # Otherwise, use optimize="size_extra"
lto="full" # Much slower build times, smaller export size

# disable_advanced_gui="yes"

# vulkan="no"      # Disables the Vulkan driver (used in Forward+/Mobile Renderers)
# use_volk="no"    # Disables more Vulkan stuff
openxr="no"      # Disables Virtual Reality/Augmented Reality stuff

# modules_enabled_by_default="no"     # Disables all modules so you can only enable what you need
module_gdscript_enabled="yes"
# module_text_server_fb_enabled="yes" # Fallback text server; less features but works fine for English.
module_noise_enabled="yes"

# https://godot-build-options-generator.github.io/
# dont know if those still exist
graphite="no"    # Disables SIL Graphite smart fonts support

module_freetype_enabled="yes"       # Needed alongside a text server for text to render correctly
module_webp_enabled="yes"
module_msdfgen_enabled="yes"
module_tinyexr_enabled = "no"

# Generated using https://godot-build-options-generator.github.io

disable_3d = "yes"
disable_navigation_2d="yes"
disable_navigation_3d="yes"
disable_xr="yes"
accesskit="yes"

deprecated = "no"
minizip = "no"
brotli = "no"

module_basis_universal_enabled = "no"
module_bmp_enabled = "no"
module_camera_enabled = "no"
module_csg_enabled = "no"
module_dds_enabled = "no"
module_enet_enabled = "no"
module_gltf_enabled = "no"
module_gridmap_enabled = "no"
module_hdr_enabled = "no"
module_jpg_enabled = "no"
module_jsonrpc_enabled = "no"
module_ktx_enabled = "no"
module_mbedtls_enabled = "no"
module_meshoptimizer_enabled = "no"
module_minimp3_enabled = "no"
module_mobile_vr_enabled = "no"
module_multiplayer_enabled = "no"
module_navigation_enabled = "no"
module_ogg_enabled = "no"
module_openxr_enabled = "no"
module_raycast_enabled = "no"
module_regex_enabled = "no"
module_squish_enabled = "no"
module_svg_enabled = "no"
module_tga_enabled = "no"
module_theora_enabled = "no"
module_upnp_enabled = "no"
module_vhacd_enabled = "no"
module_vorbis_enabled = "no"
module_webrtc_enabled = "no"
module_websocket_enabled = "no"
module_webxr_enabled = "no"
module_zip_enabled = "no"
