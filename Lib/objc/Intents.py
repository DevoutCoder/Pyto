"""
Classes from the 'Intents' framework.
"""

try:
    from rubicon.objc import ObjCClass
except ValueError:

    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None


INCarHeadUnit = _Class("INCarHeadUnit")
INCarChargingConnectorPower = _Class("INCarChargingConnectorPower")
INCallRecordFilter = _Class("INCallRecordFilter")
INSleepAlarmAttribute = _Class("INSleepAlarmAttribute")
INAlarmSearch = _Class("INAlarmSearch")
INAlarm = _Class("INAlarm")
INConnectedCall = _Class("INConnectedCall")
INWholeHouseAudioMetadata = _Class("INWholeHouseAudioMetadata")
INPrivateSearchForMediaIntentData = _Class("INPrivateSearchForMediaIntentData")
INGetSettingResponseData = _Class("INGetSettingResponseData")
INNumericSettingValue = _Class("INNumericSettingValue")
INSettingDevice = _Class("INSettingDevice")
INSettingMetadata = _Class("INSettingMetadata")
INPrivateUpdateMediaAffinityIntentData = _Class(
    "INPrivateUpdateMediaAffinityIntentData"
)
INPrivateMediaIntentData = _Class("INPrivateMediaIntentData")
INSpeakerIDInfo = _Class("INSpeakerIDInfo")
INPrivateAddMediaIntentData = _Class("INPrivateAddMediaIntentData")
INMediaSubItem = _Class("INMediaSubItem")
INBoatTrip = _Class("INBoatTrip")
INBusTrip = _Class("INBusTrip")
INPrivatePlayMediaIntentData = _Class("INPrivatePlayMediaIntentData")
INPrivateMediaItemValueData = _Class("INPrivateMediaItemValueData")
INCar = _Class("INCar")
INDeviceDetail = _Class("INDeviceDetail")
INMediaDestination = _Class("INMediaDestination")
INReservationAction = _Class("INReservationAction")
INAirportGate = _Class("INAirportGate")
INShortcutOverview = _Class("INShortcutOverview")
INAppIdentifier = _Class("INAppIdentifier")
INRentalCar = _Class("INRentalCar")
INTicketedEvent = _Class("INTicketedEvent")
INTrainTrip = _Class("INTrainTrip")
INContactEventTrigger = _Class("INContactEventTrigger")
INWidgetDescriptorManager = _Class("INWidgetDescriptorManager")
INAirline = _Class("INAirline")
INFlight = _Class("INFlight")
INAirport = _Class("INAirport")
INCodableEnumValueSynonym = _Class("INCodableEnumValueSynonym")
INSeat = _Class("INSeat")
INScoredPerson = _Class("INScoredPerson")
INHomeUserTaskResponse = _Class("INHomeUserTaskResponse")
INHomeEntityResponse = _Class("INHomeEntityResponse")
INHomeUserTask = _Class("INHomeUserTask")
INVoiceCommandStepInfo = _Class("INVoiceCommandStepInfo")
INModifyNickname = _Class("INModifyNickname")
INMediaSearch = _Class("INMediaSearch")
INHelperServiceAccessSpecifier = _Class("INHelperServiceAccessSpecifier")
INVoiceCommandDeviceInformation = _Class("INVoiceCommandDeviceInformation")
INArchivedObject = _Class("INArchivedObject")
INMessageLinkMetadata = _Class("INMessageLinkMetadata")
INHomeFilter = _Class("INHomeFilter")
INHomeContent = _Class("INHomeContent")
INTimer = _Class("INTimer")
INIntentUtilsExportHelper = _Class("INIntentUtilsExportHelper")
INStringLocalizer = _Class("INStringLocalizer")
INObjectSection = _Class("INObjectSection")
INIntentTestResult = _Class("INIntentTestResult")
INGeographicalFeature = _Class("INGeographicalFeature")
INPlace = _Class("INPlace")
INEvent = _Class("INEvent")
INIntentDeliverer = _Class("INIntentDeliverer")
INExtensionContextIntentResponseObserver = _Class(
    "INExtensionContextIntentResponseObserver"
)
INObjectCollection = _Class("INObjectCollection")
INPaymentAccount = _Class("INPaymentAccount")
INService_Subsystem = _Class("INService_Subsystem")
INDateComponentsRange = _Class("INDateComponentsRange")
_INVocabularyGenerationDiff = _Class("_INVocabularyGenerationDiff")
INImageBundle = _Class("INImageBundle")
INHomeEntity = _Class("INHomeEntity")
INImageFilePersistence = _Class("INImageFilePersistence")
INVoiceShortcut = _Class("INVoiceShortcut")
INActivity = _Class("INActivity")
INVocabulary = _Class("INVocabulary")
INJSONEncoderConfiguration = _Class("INJSONEncoderConfiguration")
_INFilePersistenceConfiguration = _Class("_INFilePersistenceConfiguration")
INRideCompletionStatus = _Class("INRideCompletionStatus")
INDefaultCardTemplate = _Class("INDefaultCardTemplate")
INAppTrust = _Class("INAppTrust")
INBillPayee = _Class("INBillPayee")
INPortableImageLoader = _Class("INPortableImageLoader")
INCache = _Class("INCache")
INNote = _Class("INNote")
INRelevantShortcut = _Class("INRelevantShortcut")
INWellnessMetadataPair = _Class("INWellnessMetadataPair")
INRestaurant = _Class("INRestaurant")
INRecurrenceRule = _Class("INRecurrenceRule")
INTemporalEventTrigger = _Class("INTemporalEventTrigger")
INCallRecord = _Class("INCallRecord")
INRidePartySizeOption = _Class("INRidePartySizeOption")
INPaymentRecord = _Class("INPaymentRecord")
INBalanceAmount = _Class("INBalanceAmount")
_INVocabularyConnection = _Class("_INVocabularyConnection")
INVocabularyUpdater = _Class("INVocabularyUpdater")
INImageServiceRegistry = _Class("INImageServiceRegistry")
INMediaItem = _Class("INMediaItem")
INImageServiceConnection = _Class("INImageServiceConnection")
_INVocabularyValidator = _Class("_INVocabularyValidator")
INJSONEncoder = _Class("INJSONEncoder")
INIntentResponseDescription = _Class("INIntentResponseDescription")
INContactRelationship = _Class("INContactRelationship")
INWidgetDescriptor = _Class("INWidgetDescriptor")
INContactCard = _Class("INContactCard")
INPriceRange = _Class("INPriceRange")
INJSONDecoder = _Class("INJSONDecoder")
INUpcomingMediaManager = _Class("INUpcomingMediaManager")
INUserContextStore = _Class("INUserContextStore")
INPaymentMethod = _Class("INPaymentMethod")
INHomeAttributeRange = _Class("INHomeAttributeRange")
_INSiriAuthorizationManager = _Class("_INSiriAuthorizationManager")
INIntentSummaryCache = _Class("INIntentSummaryCache")
INIntentSummary = _Class("INIntentSummary")
INSerializedCacheItem = _Class("INSerializedCacheItem")
INParameter = _Class("INParameter")
INRideVehicle = _Class("INRideVehicle")
INModifyRelationship = _Class("INModifyRelationship")
INRideFareLineItem = _Class("INRideFareLineItem")
INRestaurantGuestDisplayPreferences = _Class("INRestaurantGuestDisplayPreferences")
INIntentExecutionResult = _Class("INIntentExecutionResult")
INAppIntentDeliverer = _Class("INAppIntentDeliverer")
_INVocabulary = _Class("_INVocabulary")
INIntentVocabularyKnowledge = _Class("INIntentVocabularyKnowledge")
_INSyncTransaction = _Class("_INSyncTransaction")
INIntentTestResolvedParameter = _Class("INIntentTestResolvedParameter")
INHomeAttributeValue = _Class("INHomeAttributeValue")
INParameterContexts = _Class("INParameterContexts")
INRideOption = _Class("INRideOption")
INRestaurantReservationBooking = _Class("INRestaurantReservationBooking")
INRestaurantReservationUserBooking = _Class("INRestaurantReservationUserBooking")
INParameterImage = _Class("INParameterImage")
INImage = _Class("INImage")
_INBundleImage = _Class("_INBundleImage")
_INURLImage = _Class("_INURLImage")
INRemoteImageProxy = _Class("INRemoteImageProxy")
_INDataImage = _Class("_INDataImage")
INPerson = _Class("INPerson")
INRestaurantGuest = _Class("INRestaurantGuest")
INRideDriver = _Class("INRideDriver")
INHomeAttribute = _Class("INHomeAttribute")
INWellnessObjectResultValue = _Class("INWellnessObjectResultValue")
INPreferences = _Class("INPreferences")
_INVocabularyItem = _Class("_INVocabularyItem")
INIntentCodablePhrase = _Class("INIntentCodablePhrase")
INExplicitAppTrustCache = _Class("INExplicitAppTrustCache")
INRideStatus = _Class("INRideStatus")
INTask = _Class("INTask")
INFileProperty = _Class("INFileProperty")
INTermsAndConditions = _Class("INTermsAndConditions")
INNoteContent = _Class("INNoteContent")
INTextNoteContent = _Class("INTextNoteContent")
INImageNoteContent = _Class("INImageNoteContent")
INBillDetails = _Class("INBillDetails")
INIntentTest = _Class("INIntentTest")
DummyHandlerProvider = _Class("DummyHandlerProvider")
INIntentKeyParameter = _Class("INIntentKeyParameter")
INMessage = _Class("INMessage")
INSecurityScopedURL = _Class("INSecurityScopedURL")
INBundleAccessGrant = _Class("INBundleAccessGrant")
INBundleAccessManager = _Class("INBundleAccessManager")
INTaskList = _Class("INTaskList")
INHomeAction = _Class("INHomeAction")
INSpatialEventTrigger = _Class("INSpatialEventTrigger")
INReservation = _Class("INReservation")
INBoatReservation = _Class("INBoatReservation")
INBusReservation = _Class("INBusReservation")
INTrainReservation = _Class("INTrainReservation")
INFlightReservation = _Class("INFlightReservation")
INRentalCarReservation = _Class("INRentalCarReservation")
INTicketedEventReservation = _Class("INTicketedEventReservation")
INRestaurantReservation = _Class("INRestaurantReservation")
INLodgingReservation = _Class("INLodgingReservation")
INCurrencyAmount = _Class("INCurrencyAmount")
INSendMessageAttachment = _Class("INSendMessageAttachment")
INPersonHandle = _Class("INPersonHandle")
INExtensionContextSlotResolutionResult = _Class(
    "INExtensionContextSlotResolutionResult"
)
INRestaurantOffer = _Class("INRestaurantOffer")
INUserContext = _Class("INUserContext")
INMediaUserContext = _Class("INMediaUserContext")
_INVocabularyGenerationDocument = _Class("_INVocabularyGenerationDocument")
INExtension = _Class("INExtension")
_INExtension = _Class("_INExtension")
INIntentForwardingAction = _Class("INIntentForwardingAction")
INHandleIntentForwardingAction = _Class("INHandleIntentForwardingAction")
INStartSendingUpdatesForwardingAction = _Class("INStartSendingUpdatesForwardingAction")
INStopSendingUpdatesForwardingAction = _Class("INStopSendingUpdatesForwardingAction")
INConfirmIntentForwardingAction = _Class("INConfirmIntentForwardingAction")
INGetIntentParameterDefaultValueForwardingAction = _Class(
    "INGetIntentParameterDefaultValueForwardingAction"
)
INGetIntentParameterOptionsForwardingAction = _Class(
    "INGetIntentParameterOptionsForwardingAction"
)
INResolveIntentParametersForwardingAction = _Class(
    "INResolveIntentParametersForwardingAction"
)
INRelevantShortcutStore = _Class("INRelevantShortcutStore")
INRelevanceProvider = _Class("INRelevanceProvider")
INDateRelevanceProvider = _Class("INDateRelevanceProvider")
INDailyRoutineRelevanceProvider = _Class("INDailyRoutineRelevanceProvider")
INLocationRelevanceProvider = _Class("INLocationRelevanceProvider")
INPaymentAmount = _Class("INPaymentAmount")
_INVocabularyStoreManager = _Class("_INVocabularyStoreManager")
INExtensionContext = _Class("INExtensionContext")
INExecutionCounterpartMapper = _Class("INExecutionCounterpartMapper")
_INAggregator = _Class("_INAggregator")
INIntentForwardingActionResponse = _Class("INIntentForwardingActionResponse")
INConfirmIntentForwardingActionResponse = _Class(
    "INConfirmIntentForwardingActionResponse"
)
INHandleIntentForwardingActionResponse = _Class(
    "INHandleIntentForwardingActionResponse"
)
INGetIntentParameterOptionsForwardingActionResponse = _Class(
    "INGetIntentParameterOptionsForwardingActionResponse"
)
INResolveIntentParametersForwardingActionResponse = _Class(
    "INResolveIntentParametersForwardingActionResponse"
)
INGetIntentParameterDefaultValueForwardingActionResponse = _Class(
    "INGetIntentParameterDefaultValueForwardingActionResponse"
)
INKeyImageExtraction = _Class("INKeyImageExtraction")
INVoiceShortcutCenter = _Class("INVoiceShortcutCenter")
INShortcut = _Class("INShortcut")
INWatchdogTimer = _Class("INWatchdogTimer")
INAppInfo = _Class("INAppInfo")
INIntentResolutionResult = _Class("INIntentResolutionResult")
INCallRecordResolutionResult = _Class("INCallRecordResolutionResult")
INStartCallCallRecordToCallBackResolutionResult = _Class(
    "INStartCallCallRecordToCallBackResolutionResult"
)
INAlarmSearchTypeResolutionResult = _Class("INAlarmSearchTypeResolutionResult")
INAlarmRepeatScheduleOptionsResolutionResult = _Class(
    "INAlarmRepeatScheduleOptionsResolutionResult"
)
INChangeAlarmStatusOperationResolutionResult = _Class(
    "INChangeAlarmStatusOperationResolutionResult"
)
INUpdateAlarmOperationResolutionResult = _Class(
    "INUpdateAlarmOperationResolutionResult"
)
INAlarmResolutionResult = _Class("INAlarmResolutionResult")
INSearchAlarmAlarmResolutionResult = _Class("INSearchAlarmAlarmResolutionResult")
INUpdateAlarmAlarmResolutionResult = _Class("INUpdateAlarmAlarmResolutionResult")
INChangeAlarmStatusAlarmResolutionResult = _Class(
    "INChangeAlarmStatusAlarmResolutionResult"
)
INDeleteAlarmAlarmResolutionResult = _Class("INDeleteAlarmAlarmResolutionResult")
INSnoozeAlarmAlarmResolutionResult = _Class("INSnoozeAlarmAlarmResolutionResult")
INOutgoingMessageTypeResolutionResult = _Class("INOutgoingMessageTypeResolutionResult")
INBinarySettingValueResolutionResult = _Class("INBinarySettingValueResolutionResult")
INBoundedSettingValueResolutionResult = _Class("INBoundedSettingValueResolutionResult")
INSettingMetadataResolutionResult = _Class("INSettingMetadataResolutionResult")
INNumericSettingValueResolutionResult = _Class("INNumericSettingValueResolutionResult")
INSettingActionResolutionResult = _Class("INSettingActionResolutionResult")
INDeviceDetailResolutionResult = _Class("INDeviceDetailResolutionResult")
INFindDeviceAndPlaySoundDeviceResolutionResult = _Class(
    "INFindDeviceAndPlaySoundDeviceResolutionResult"
)
INMediaDestinationResolutionResult = _Class("INMediaDestinationResolutionResult")
INAddMediaMediaDestinationResolutionResult = _Class(
    "INAddMediaMediaDestinationResolutionResult"
)
INAppIdentifierResolutionResult = _Class("INAppIdentifierResolutionResult")
INIntentExecutionResultResolutionResult = _Class(
    "INIntentExecutionResultResolutionResult"
)
INTaskPriorityResolutionResult = _Class("INTaskPriorityResolutionResult")
INModifyNicknameResolutionResult = _Class("INModifyNicknameResolutionResult")
INTemporalEventTriggerTypeOptionsResolutionResult = _Class(
    "INTemporalEventTriggerTypeOptionsResolutionResult"
)
INContactEventTriggerResolutionResult = _Class("INContactEventTriggerResolutionResult")
INSetTaskAttributeContactEventTriggerResolutionResult = _Class(
    "INSetTaskAttributeContactEventTriggerResolutionResult"
)
INAddTasksContactEventTriggerResolutionResult = _Class(
    "INAddTasksContactEventTriggerResolutionResult"
)
INTaskReferenceResolutionResult = _Class("INTaskReferenceResolutionResult")
INCallCapabilityResolutionResult = _Class("INCallCapabilityResolutionResult")
INStartCallCallCapabilityResolutionResult = _Class(
    "INStartCallCallCapabilityResolutionResult"
)
INPreferredCallProviderResolutionResult = _Class(
    "INPreferredCallProviderResolutionResult"
)
INStartCallPreferredCallProviderResolutionResult = _Class(
    "INStartCallPreferredCallProviderResolutionResult"
)
INPaymentMethodResolutionResult = _Class("INPaymentMethodResolutionResult")
INHomeUserTaskResolutionResult = _Class("INHomeUserTaskResolutionResult")
INHomeFilterResolutionResult = _Class("INHomeFilterResolutionResult")
INMessageEffectTypeResolutionResult = _Class("INMessageEffectTypeResolutionResult")
INMediaAffinityTypeResolutionResult = _Class("INMediaAffinityTypeResolutionResult")
INPlaybackRepeatModeResolutionResult = _Class("INPlaybackRepeatModeResolutionResult")
INPlaybackQueueLocationResolutionResult = _Class(
    "INPlaybackQueueLocationResolutionResult"
)
INMediaItemResolutionResult = _Class("INMediaItemResolutionResult")
INUpdateMediaAffinityMediaItemResolutionResult = _Class(
    "INUpdateMediaAffinityMediaItemResolutionResult"
)
INSearchForMediaMediaItemResolutionResult = _Class(
    "INSearchForMediaMediaItemResolutionResult"
)
INAddMediaMediaItemResolutionResult = _Class("INAddMediaMediaItemResolutionResult")
INPlayMediaMediaItemResolutionResult = _Class("INPlayMediaMediaItemResolutionResult")
INTimerStateResolutionResult = _Class("INTimerStateResolutionResult")
INTimerResolutionResult = _Class("INTimerResolutionResult")
INSetTimerAttributeTargetTimerResolutionResult = _Class(
    "INSetTimerAttributeTargetTimerResolutionResult"
)
INModifyRelationshipResolutionResult = _Class("INModifyRelationshipResolutionResult")
INMassResolutionResult = _Class("INMassResolutionResult")
INCallRecordTypeOptionsResolutionResult = _Class(
    "INCallRecordTypeOptionsResolutionResult"
)
INRestaurantGuestResolutionResult = _Class("INRestaurantGuestResolutionResult")
INNotebookItemTypeResolutionResult = _Class("INNotebookItemTypeResolutionResult")
INCarAirCirculationModeResolutionResult = _Class(
    "INCarAirCirculationModeResolutionResult"
)
INWellnessQuestionTypeResolutionResult = _Class(
    "INWellnessQuestionTypeResolutionResult"
)
INBillPayeeResolutionResult = _Class("INBillPayeeResolutionResult")
INCallRecordTypeResolutionResult = _Class("INCallRecordTypeResolutionResult")
INIntegerResolutionResult = _Class("INIntegerResolutionResult")
INRestaurantResolutionResult = _Class("INRestaurantResolutionResult")
INEnergyResolutionResult = _Class("INEnergyResolutionResult")
INObjectResolutionResult = _Class("INObjectResolutionResult")
INNoteResolutionResult = _Class("INNoteResolutionResult")
INVisualCodeTypeResolutionResult = _Class("INVisualCodeTypeResolutionResult")
INWorkoutLocationTypeResolutionResult = _Class("INWorkoutLocationTypeResolutionResult")
INRadioTypeResolutionResult = _Class("INRadioTypeResolutionResult")
INRelativeSettingResolutionResult = _Class("INRelativeSettingResolutionResult")
INCarAudioSourceResolutionResult = _Class("INCarAudioSourceResolutionResult")
INRelativeReferenceResolutionResult = _Class("INRelativeReferenceResolutionResult")
INBooleanResolutionResult = _Class("INBooleanResolutionResult")
INDateSearchTypeResolutionResult = _Class("INDateSearchTypeResolutionResult")
INTaskStatusResolutionResult = _Class("INTaskStatusResolutionResult")
INPaymentAccountResolutionResult = _Class("INPaymentAccountResolutionResult")
INHealthUnitResolutionResult = _Class("INHealthUnitResolutionResult")
INDateComponentsResolutionResult = _Class("INDateComponentsResolutionResult")
INLocationSearchTypeResolutionResult = _Class("INLocationSearchTypeResolutionResult")
INNoteContentTypeResolutionResult = _Class("INNoteContentTypeResolutionResult")
INPlacemarkResolutionResult = _Class("INPlacemarkResolutionResult")
INSpeedResolutionResult = _Class("INSpeedResolutionResult")
INSpeakableStringResolutionResult = _Class("INSpeakableStringResolutionResult")
INRunWorkflowWorkflowResolutionResult = _Class("INRunWorkflowWorkflowResolutionResult")
INCreateTimerLabelResolutionResult = _Class("INCreateTimerLabelResolutionResult")
INTaskListResolutionResult = _Class("INTaskListResolutionResult")
INDeleteTasksTaskListResolutionResult = _Class("INDeleteTasksTaskListResolutionResult")
INAddTasksTargetTaskListResolutionResult = _Class(
    "INAddTasksTargetTaskListResolutionResult"
)
INTemporalEventTriggerResolutionResult = _Class(
    "INTemporalEventTriggerResolutionResult"
)
INSetTaskAttributeTemporalEventTriggerResolutionResult = _Class(
    "INSetTaskAttributeTemporalEventTriggerResolutionResult"
)
INAddTasksTemporalEventTriggerResolutionResult = _Class(
    "INAddTasksTemporalEventTriggerResolutionResult"
)
INTimeIntervalResolutionResult = _Class("INTimeIntervalResolutionResult")
INTemperatureResolutionResult = _Class("INTemperatureResolutionResult")
INPaymentAmountResolutionResult = _Class("INPaymentAmountResolutionResult")
INBalanceTypeResolutionResult = _Class("INBalanceTypeResolutionResult")
INTimerTypeResolutionResult = _Class("INTimerTypeResolutionResult")
INWorkoutGoalUnitTypeResolutionResult = _Class("INWorkoutGoalUnitTypeResolutionResult")
INNoteContentResolutionResult = _Class("INNoteContentResolutionResult")
INCurrencyAmountResolutionResult = _Class("INCurrencyAmountResolutionResult")
INSendPaymentCurrencyAmountResolutionResult = _Class(
    "INSendPaymentCurrencyAmountResolutionResult"
)
INRequestPaymentCurrencyAmountResolutionResult = _Class(
    "INRequestPaymentCurrencyAmountResolutionResult"
)
INPaymentStatusResolutionResult = _Class("INPaymentStatusResolutionResult")
INBillTypeResolutionResult = _Class("INBillTypeResolutionResult")
INTaskResolutionResult = _Class("INTaskResolutionResult")
INDeleteTasksTaskResolutionResult = _Class("INDeleteTasksTaskResolutionResult")
INSnoozeTasksTaskResolutionResult = _Class("INSnoozeTasksTaskResolutionResult")
INCarSignalOptionsResolutionResult = _Class("INCarSignalOptionsResolutionResult")
INPersonResolutionResult = _Class("INPersonResolutionResult")
INStopShareETARecipientResolutionResult = _Class(
    "INStopShareETARecipientResolutionResult"
)
INShareETARecipientResolutionResult = _Class("INShareETARecipientResolutionResult")
INAddTasksTargetTaskListMemberResolutionResult = _Class(
    "INAddTasksTargetTaskListMemberResolutionResult"
)
INStartCallContactResolutionResult = _Class("INStartCallContactResolutionResult")
INRequestPaymentPayerResolutionResult = _Class("INRequestPaymentPayerResolutionResult")
INSendPaymentPayeeResolutionResult = _Class("INSendPaymentPayeeResolutionResult")
INSendMessageRecipientResolutionResult = _Class(
    "INSendMessageRecipientResolutionResult"
)
INDoubleResolutionResult = _Class("INDoubleResolutionResult")
INPlayMediaPlaybackSpeedResolutionResult = _Class(
    "INPlayMediaPlaybackSpeedResolutionResult"
)
INWellnessObjectTypeResolutionResult = _Class("INWellnessObjectTypeResolutionResult")
INLengthResolutionResult = _Class("INLengthResolutionResult")
INCarDefrosterResolutionResult = _Class("INCarDefrosterResolutionResult")
INEnumResolutionResult = _Class("INEnumResolutionResult")
INWellnessMetadataPairResolutionResult = _Class(
    "INWellnessMetadataPairResolutionResult"
)
INDateComponentsRangeResolutionResult = _Class("INDateComponentsRangeResolutionResult")
INSaveHealthSampleRecordDateResolutionResult = _Class(
    "INSaveHealthSampleRecordDateResolutionResult"
)
INCarSeatResolutionResult = _Class("INCarSeatResolutionResult")
INVolumeResolutionResult = _Class("INVolumeResolutionResult")
INAccountTypeResolutionResult = _Class("INAccountTypeResolutionResult")
INMessageAttributeResolutionResult = _Class("INMessageAttributeResolutionResult")
INWellnessQueryResultTypeResolutionResult = _Class(
    "INWellnessQueryResultTypeResolutionResult"
)
INURLResolutionResult = _Class("INURLResolutionResult")
INCallDestinationTypeResolutionResult = _Class("INCallDestinationTypeResolutionResult")
INMessageAttributeOptionsResolutionResult = _Class(
    "INMessageAttributeOptionsResolutionResult"
)
INSpatialEventTriggerResolutionResult = _Class("INSpatialEventTriggerResolutionResult")
INNumberResolutionResult = _Class("INNumberResolutionResult")
INFileResolutionResult = _Class("INFileResolutionResult")
INStringResolutionResult = _Class("INStringResolutionResult")
INIntentSlotDescription = _Class("INIntentSlotDescription")
INIntentDescription = _Class("INIntentDescription")
INObject = _Class("INObject")
INCustomObject = _Class("INCustomObject")
INSpeakableString = _Class("INSpeakableString")
INFile = _Class("INFile")
INCodableEnumValue = _Class("INCodableEnumValue")
INCodableEnum = _Class("INCodableEnum")
INIntentResponse = _Class("INIntentResponse")
INSearchAlarmIntentResponse = _Class("INSearchAlarmIntentResponse")
INUpdateAlarmIntentResponse = _Class("INUpdateAlarmIntentResponse")
INChangeAlarmStatusIntentResponse = _Class("INChangeAlarmStatusIntentResponse")
INSnoozeAlarmIntentResponse = _Class("INSnoozeAlarmIntentResponse")
INCreateAlarmIntentResponse = _Class("INCreateAlarmIntentResponse")
INDeleteAlarmIntentResponse = _Class("INDeleteAlarmIntentResponse")
INOpenSettingIntentResponse = _Class("INOpenSettingIntentResponse")
INSaveParkingLocationIntentResponse = _Class("INSaveParkingLocationIntentResponse")
INDeleteParkingLocationIntentResponse = _Class("INDeleteParkingLocationIntentResponse")
INSetBinarySettingIntentResponse = _Class("INSetBinarySettingIntentResponse")
INSetLabeledSettingIntentResponse = _Class("INSetLabeledSettingIntentResponse")
INSetTemporalSettingIntentResponse = _Class("INSetTemporalSettingIntentResponse")
INGetSettingIntentResponse = _Class("INGetSettingIntentResponse")
INSetNumericSettingIntentResponse = _Class("INSetNumericSettingIntentResponse")
INStopShareETAIntentResponse = _Class("INStopShareETAIntentResponse")
INShareETAIntentResponse = _Class("INShareETAIntentResponse")
INRetrieveParkingLocationIntentResponse = _Class(
    "INRetrieveParkingLocationIntentResponse"
)
INSetNicknameIntentResponse = _Class("INSetNicknameIntentResponse")
INSetRelationshipIntentResponse = _Class("INSetRelationshipIntentResponse")
INSearchForContactIntentResponse = _Class("INSearchForContactIntentResponse")
INSearchForMeCardIntentResponse = _Class("INSearchForMeCardIntentResponse")
INListCarsIntentResponse = _Class("INListCarsIntentResponse")
INFindDeviceAndPlaySoundIntentResponse = _Class(
    "INFindDeviceAndPlaySoundIntentResponse"
)
INPlayMessageSoundIntentResponse = _Class("INPlayMessageSoundIntentResponse")
INListShortcutsIntentResponse = _Class("INListShortcutsIntentResponse")
INGetReservationDetailsIntentResponse = _Class("INGetReservationDetailsIntentResponse")
INDeleteTasksIntentResponse = _Class("INDeleteTasksIntentResponse")
INSnoozeTasksIntentResponse = _Class("INSnoozeTasksIntentResponse")
INShowHomeIntentResponse = _Class("INShowHomeIntentResponse")
INStartCallIntentResponse = _Class("INStartCallIntentResponse")
INHangUpCallIntentResponse = _Class("INHangUpCallIntentResponse")
INAnswerCallIntentResponse = _Class("INAnswerCallIntentResponse")
INIdentifyIncomingCallerIntentResponse = _Class(
    "INIdentifyIncomingCallerIntentResponse"
)
INSearchForMediaIntentResponse = _Class("INSearchForMediaIntentResponse")
INAddMediaIntentResponse = _Class("INAddMediaIntentResponse")
INUpdateMediaAffinityIntentResponse = _Class("INUpdateMediaAffinityIntentResponse")
INRunWorkflowIntentResponse = _Class("INRunWorkflowIntentResponse")
INSearchForTimersIntentResponse = _Class("INSearchForTimersIntentResponse")
INPauseTimerIntentResponse = _Class("INPauseTimerIntentResponse")
INDeleteTimerIntentResponse = _Class("INDeleteTimerIntentResponse")
INCreateTimerIntentResponse = _Class("INCreateTimerIntentResponse")
INResetTimerIntentResponse = _Class("INResetTimerIntentResponse")
INResumeTimerIntentResponse = _Class("INResumeTimerIntentResponse")
INSetTimerAttributeIntentResponse = _Class("INSetTimerAttributeIntentResponse")
INPlayMediaIntentResponse = _Class("INPlayMediaIntentResponse")
INCreateTaskListIntentResponse = _Class("INCreateTaskListIntentResponse")
INGetAvailableRestaurantReservationBookingDefaultsIntentResponse = _Class(
    "INGetAvailableRestaurantReservationBookingDefaultsIntentResponse"
)
INSearchForAccountsIntentResponse = _Class("INSearchForAccountsIntentResponse")
INCancelWorkoutIntentResponse = _Class("INCancelWorkoutIntentResponse")
INSaveProfileInCarIntentResponse = _Class("INSaveProfileInCarIntentResponse")
INRequestPaymentIntentResponse = _Class("INRequestPaymentIntentResponse")
INPauseWorkoutIntentResponse = _Class("INPauseWorkoutIntentResponse")
INBookRestaurantReservationIntentResponse = _Class(
    "INBookRestaurantReservationIntentResponse"
)
INSendPaymentIntentResponse = _Class("INSendPaymentIntentResponse")
INGetCarLockStatusIntentResponse = _Class("INGetCarLockStatusIntentResponse")
INGetCarPowerLevelStatusIntentResponse = _Class(
    "INGetCarPowerLevelStatusIntentResponse"
)
INPlayVoicemailIntentResponse = _Class("INPlayVoicemailIntentResponse")
INScanVisualCodeIntentResponse = _Class("INScanVisualCodeIntentResponse")
INSendRideFeedbackIntentResponse = _Class("INSendRideFeedbackIntentResponse")
INSendMessageIntentResponse = _Class("INSendMessageIntentResponse")
INGetUserCurrentRestaurantReservationBookingsIntentResponse = _Class(
    "INGetUserCurrentRestaurantReservationBookingsIntentResponse"
)
INDeleteHealthSampleIntentResponse = _Class("INDeleteHealthSampleIntentResponse")
INSetCarLockStatusIntentResponse = _Class("INSetCarLockStatusIntentResponse")
INCreateNoteIntentResponse = _Class("INCreateNoteIntentResponse")
INStartVideoCallIntentResponse = _Class("INStartVideoCallIntentResponse")
INPayBillIntentResponse = _Class("INPayBillIntentResponse")
INSetTaskAttributeIntentResponse = _Class("INSetTaskAttributeIntentResponse")
INSearchForBillsIntentResponse = _Class("INSearchForBillsIntentResponse")
INSearchForMessagesIntentResponse = _Class("INSearchForMessagesIntentResponse")
INSetClimateSettingsInCarIntentResponse = _Class(
    "INSetClimateSettingsInCarIntentResponse"
)
INSearchForNotebookItemsIntentResponse = _Class(
    "INSearchForNotebookItemsIntentResponse"
)
INStartAudioCallIntentResponse = _Class("INStartAudioCallIntentResponse")
INQueryHealthSampleIntentResponse = _Class("INQueryHealthSampleIntentResponse")
INGetRideStatusIntentResponse = _Class("INGetRideStatusIntentResponse")
INListRideOptionsIntentResponse = _Class("INListRideOptionsIntentResponse")
INSearchForPhotosIntentResponse = _Class("INSearchForPhotosIntentResponse")
INGetVisualCodeIntentResponse = _Class("INGetVisualCodeIntentResponse")
INSetSeatSettingsInCarIntentResponse = _Class("INSetSeatSettingsInCarIntentResponse")
INSetDefrosterSettingsInCarIntentResponse = _Class(
    "INSetDefrosterSettingsInCarIntentResponse"
)
INSetProfileInCarIntentResponse = _Class("INSetProfileInCarIntentResponse")
INSetAudioSourceInCarIntentResponse = _Class("INSetAudioSourceInCarIntentResponse")
INSearchCallHistoryIntentResponse = _Class("INSearchCallHistoryIntentResponse")
INRequestRideIntentResponse = _Class("INRequestRideIntentResponse")
INResumeWorkoutIntentResponse = _Class("INResumeWorkoutIntentResponse")
INControlHomeIntentResponse = _Class("INControlHomeIntentResponse")
INEndWorkoutIntentResponse = _Class("INEndWorkoutIntentResponse")
INTransferMoneyIntentResponse = _Class("INTransferMoneyIntentResponse")
INConfigureHomeIntentResponse = _Class("INConfigureHomeIntentResponse")
INPlayAudioMessageIntentResponse = _Class("INPlayAudioMessageIntentResponse")
INSaveHealthSampleIntentResponse = _Class("INSaveHealthSampleIntentResponse")
INSetRadioStationIntentResponse = _Class("INSetRadioStationIntentResponse")
INRunVoiceCommandIntentResponse = _Class("INRunVoiceCommandIntentResponse")
INAddTasksIntentResponse = _Class("INAddTasksIntentResponse")
INStartWorkoutIntentResponse = _Class("INStartWorkoutIntentResponse")
INAppendToNoteIntentResponse = _Class("INAppendToNoteIntentResponse")
INCancelRideIntentResponse = _Class("INCancelRideIntentResponse")
INSetMessageAttributeIntentResponse = _Class("INSetMessageAttributeIntentResponse")
INActivateCarSignalIntentResponse = _Class("INActivateCarSignalIntentResponse")
INGetRestaurantGuestIntentResponse = _Class("INGetRestaurantGuestIntentResponse")
INQueryHomeIntentResponse = _Class("INQueryHomeIntentResponse")
INGetAvailableRestaurantReservationBookingsIntentResponse = _Class(
    "INGetAvailableRestaurantReservationBookingsIntentResponse"
)
INStartPhotoPlaybackIntentResponse = _Class("INStartPhotoPlaybackIntentResponse")
INIntentResponseCodableCode = _Class("INIntentResponseCodableCode")
INCodableAttributeRelationship = _Class("INCodableAttributeRelationship")
INCodableAttributeMetadata = _Class("INCodableAttributeMetadata")
INCodableTimeIntervalAttributeMetadata = _Class(
    "INCodableTimeIntervalAttributeMetadata"
)
INCodableEnumAttributeMetadata = _Class("INCodableEnumAttributeMetadata")
INCodableBooleanAttributeMetadata = _Class("INCodableBooleanAttributeMetadata")
INCodableDateComponentsAttributeMetadata = _Class(
    "INCodableDateComponentsAttributeMetadata"
)
INCodableURLAttributeMetadata = _Class("INCodableURLAttributeMetadata")
INCodablePersonAttributeMetadata = _Class("INCodablePersonAttributeMetadata")
INCodableFileAttributeMetadata = _Class("INCodableFileAttributeMetadata")
INCodablePlacemarkAttributeMetadata = _Class("INCodablePlacemarkAttributeMetadata")
INCodableStringAttributeMetadata = _Class("INCodableStringAttributeMetadata")
INCodableMeasurementAttributeMetadata = _Class("INCodableMeasurementAttributeMetadata")
INCodableNumberAttributeMetadata = _Class("INCodableNumberAttributeMetadata")
INCodableDecimalAttributeMetadata = _Class("INCodableDecimalAttributeMetadata")
INCodableCurrencyAmountAttributeMetadata = _Class(
    "INCodableCurrencyAmountAttributeMetadata"
)
INCodableIntegerAttributeMetadata = _Class("INCodableIntegerAttributeMetadata")
INCodableAttributeDialog = _Class("INCodableAttributeDialog")
INCodableAttributeUnsupportedReason = _Class("INCodableAttributeUnsupportedReason")
INCodableAttributePromptDialog = _Class("INCodableAttributePromptDialog")
INCodableAttribute = _Class("INCodableAttribute")
INCodableEnumAttribute = _Class("INCodableEnumAttribute")
INCodableObjectAttribute = _Class("INCodableObjectAttribute")
INCodableCustomObjectAttribute = _Class("INCodableCustomObjectAttribute")
INCodableScalarAttribute = _Class("INCodableScalarAttribute")
INCodableDescription = _Class("INCodableDescription")
INTypeCodableDescription = _Class("INTypeCodableDescription")
INRootCodableDescription = _Class("INRootCodableDescription")
INIntentResponseCodableDescription = _Class("INIntentResponseCodableDescription")
INIntentCodableDescription = _Class("INIntentCodableDescription")
INCodableLocalizationTable = _Class("INCodableLocalizationTable")
INParameterCombination = _Class("INParameterCombination")
INExecutionInfoResolver = _Class("INExecutionInfoResolver")
INExecutionInfo = _Class("INExecutionInfo")
INIntentExecutionInfo = _Class("INIntentExecutionInfo")
INUserActivityExecutionInfo = _Class("INUserActivityExecutionInfo")
INSchema = _Class("INSchema")
INIntent = _Class("INIntent")
INSearchAlarmIntent = _Class("INSearchAlarmIntent")
INCreateAlarmIntent = _Class("INCreateAlarmIntent")
INChangeAlarmStatusIntent = _Class("INChangeAlarmStatusIntent")
INDeleteAlarmIntent = _Class("INDeleteAlarmIntent")
INSnoozeAlarmIntent = _Class("INSnoozeAlarmIntent")
INUpdateAlarmIntent = _Class("INUpdateAlarmIntent")
INOpenSettingIntent = _Class("INOpenSettingIntent")
INDeleteParkingLocationIntent = _Class("INDeleteParkingLocationIntent")
INSaveParkingLocationIntent = _Class("INSaveParkingLocationIntent")
INSetLabeledSettingIntent = _Class("INSetLabeledSettingIntent")
INSetNumericSettingIntent = _Class("INSetNumericSettingIntent")
INSetTemporalSettingIntent = _Class("INSetTemporalSettingIntent")
INGetSettingIntent = _Class("INGetSettingIntent")
INSetBinarySettingIntent = _Class("INSetBinarySettingIntent")
INShareETAIntent = _Class("INShareETAIntent")
INStopShareETAIntent = _Class("INStopShareETAIntent")
INRetrieveParkingLocationIntent = _Class("INRetrieveParkingLocationIntent")
INSetNicknameIntent = _Class("INSetNicknameIntent")
INSetRelationshipIntent = _Class("INSetRelationshipIntent")
INSearchForContactIntent = _Class("INSearchForContactIntent")
INSearchForMeCardIntent = _Class("INSearchForMeCardIntent")
INListCarsIntent = _Class("INListCarsIntent")
INFindDeviceAndPlaySoundIntent = _Class("INFindDeviceAndPlaySoundIntent")
INPlayMessageSoundIntent = _Class("INPlayMessageSoundIntent")
INListShortcutsIntent = _Class("INListShortcutsIntent")
INDeleteTasksIntent = _Class("INDeleteTasksIntent")
INSnoozeTasksIntent = _Class("INSnoozeTasksIntent")
INShowHomeIntent = _Class("INShowHomeIntent")
INHangUpCallIntent = _Class("INHangUpCallIntent")
INIdentifyIncomingCallerIntent = _Class("INIdentifyIncomingCallerIntent")
INAnswerCallIntent = _Class("INAnswerCallIntent")
INSearchForMediaIntent = _Class("INSearchForMediaIntent")
INAddMediaIntent = _Class("INAddMediaIntent")
INUpdateMediaAffinityIntent = _Class("INUpdateMediaAffinityIntent")
INRunWorkflowIntent = _Class("INRunWorkflowIntent")
INSearchForTimersIntent = _Class("INSearchForTimersIntent")
INResetTimerIntent = _Class("INResetTimerIntent")
INDeleteTimerIntent = _Class("INDeleteTimerIntent")
INSetTimerAttributeIntent = _Class("INSetTimerAttributeIntent")
INPauseTimerIntent = _Class("INPauseTimerIntent")
INCreateTimerIntent = _Class("INCreateTimerIntent")
INResumeTimerIntent = _Class("INResumeTimerIntent")
INPlayMediaIntent = _Class("INPlayMediaIntent")
INSearchForAccountsIntent = _Class("INSearchForAccountsIntent")
INSaveProfileInCarIntent = _Class("INSaveProfileInCarIntent")
INAddTasksIntent = _Class("INAddTasksIntent")
INCreateNoteIntent = _Class("INCreateNoteIntent")
INStartWorkoutIntent = _Class("INStartWorkoutIntent")
INResumeWorkoutIntent = _Class("INResumeWorkoutIntent")
INAppendToNoteIntent = _Class("INAppendToNoteIntent")
INSearchForPhotosIntent = _Class("INSearchForPhotosIntent")
INRunVoiceCommandIntent = _Class("INRunVoiceCommandIntent")
INSearchForBillsIntent = _Class("INSearchForBillsIntent")
INSearchForMessagesIntent = _Class("INSearchForMessagesIntent")
INSetSeatSettingsInCarIntent = _Class("INSetSeatSettingsInCarIntent")
INSearchCallHistoryIntent = _Class("INSearchCallHistoryIntent")
INQueryHealthSampleIntent = _Class("INQueryHealthSampleIntent")
INSetMessageAttributeIntent = _Class("INSetMessageAttributeIntent")
INSetClimateSettingsInCarIntent = _Class("INSetClimateSettingsInCarIntent")
INSaveHealthSampleIntent = _Class("INSaveHealthSampleIntent")
INGetCarPowerLevelStatusIntent = _Class("INGetCarPowerLevelStatusIntent")
INQueryHomeIntent = _Class("INQueryHomeIntent")
INSendRideFeedbackIntent = _Class("INSendRideFeedbackIntent")
INRequestPaymentIntent = _Class("INRequestPaymentIntent")
INGetVisualCodeIntent = _Class("INGetVisualCodeIntent")
INBookRestaurantReservationIntent = _Class("INBookRestaurantReservationIntent")
INPlayAudioMessageIntent = _Class("INPlayAudioMessageIntent")
INPlayVoicemailIntent = _Class("INPlayVoicemailIntent")
INSendMessageIntent = _Class("INSendMessageIntent")
INCancelWorkoutIntent = _Class("INCancelWorkoutIntent")
INScanVisualCodeIntent = _Class("INScanVisualCodeIntent")
INShowPersonInteractionsIntent = _Class("INShowPersonInteractionsIntent")
INSetDefrosterSettingsInCarIntent = _Class("INSetDefrosterSettingsInCarIntent")
INStartAudioCallIntent = _Class("INStartAudioCallIntent")
INSetRadioStationIntent = _Class("INSetRadioStationIntent")
INPauseWorkoutIntent = _Class("INPauseWorkoutIntent")
INDeleteHealthSampleIntent = _Class("INDeleteHealthSampleIntent")
INGetRideStatusIntent = _Class("INGetRideStatusIntent")
INSendPaymentIntent = _Class("INSendPaymentIntent")
INGetAvailableRestaurantReservationBookingsIntent = _Class(
    "INGetAvailableRestaurantReservationBookingsIntent"
)
INSearchForNotebookItemsIntent = _Class("INSearchForNotebookItemsIntent")
INPayBillIntent = _Class("INPayBillIntent")
INGetUserCurrentRestaurantReservationBookingsIntent = _Class(
    "INGetUserCurrentRestaurantReservationBookingsIntent"
)
INActivateCarSignalIntent = _Class("INActivateCarSignalIntent")
INSetTaskAttributeIntent = _Class("INSetTaskAttributeIntent")
INSetCarLockStatusIntent = _Class("INSetCarLockStatusIntent")
INCancelRideIntent = _Class("INCancelRideIntent")
INGetRestaurantGuestIntent = _Class("INGetRestaurantGuestIntent")
INControlHomeIntent = _Class("INControlHomeIntent")
INStartPhotoPlaybackIntent = _Class("INStartPhotoPlaybackIntent")
INListRideOptionsIntent = _Class("INListRideOptionsIntent")
INRequestRideIntent = _Class("INRequestRideIntent")
INGetAvailableRestaurantReservationBookingDefaultsIntent = _Class(
    "INGetAvailableRestaurantReservationBookingDefaultsIntent"
)
INConfigureHomeIntent = _Class("INConfigureHomeIntent")
INGetCarLockStatusIntent = _Class("INGetCarLockStatusIntent")
INEndWorkoutIntent = _Class("INEndWorkoutIntent")
INCreateTaskListIntent = _Class("INCreateTaskListIntent")
INSetAudioSourceInCarIntent = _Class("INSetAudioSourceInCarIntent")
INStartVideoCallIntent = _Class("INStartVideoCallIntent")
INTransferMoneyIntent = _Class("INTransferMoneyIntent")
INSetProfileInCarIntent = _Class("INSetProfileInCarIntent")
INGetReservationDetailsIntent = _Class("INGetReservationDetailsIntent")
INStartCallIntent = _Class("INStartCallIntent")
INInteraction = _Class("INInteraction")
_INPBCarHeadUnit = _Class("_INPBCarHeadUnit")
_INPBCarChargingConnectorPower = _Class("_INPBCarChargingConnectorPower")
_INPBPower = _Class("_INPBPower")
_INPBCallRecordFilter = _Class("_INPBCallRecordFilter")
_INPBJSONDictionary = _Class("_INPBJSONDictionary")
_INPBPowerValue = _Class("_INPBPowerValue")
_INPBBoatReservation = _Class("_INPBBoatReservation")
_INPBBusReservation = _Class("_INPBBusReservation")
_INPBSearchAlarmIntentResponse = _Class("_INPBSearchAlarmIntentResponse")
_INPBSearchAlarmIntent = _Class("_INPBSearchAlarmIntent")
_INPBSleepAlarmAttribute = _Class("_INPBSleepAlarmAttribute")
_INPBDeleteAlarmIntentResponse = _Class("_INPBDeleteAlarmIntentResponse")
_INPBAlarm = _Class("_INPBAlarm")
_INPBChangeAlarmStatusIntentResponse = _Class("_INPBChangeAlarmStatusIntentResponse")
_INPBSnoozeAlarmIntentResponse = _Class("_INPBSnoozeAlarmIntentResponse")
_INPBCreateAlarmIntentResponse = _Class("_INPBCreateAlarmIntentResponse")
_INPBDeleteAlarmIntent = _Class("_INPBDeleteAlarmIntent")
_INPBChangeAlarmStatusIntent = _Class("_INPBChangeAlarmStatusIntent")
_INPBUpdateAlarmIntentResponse = _Class("_INPBUpdateAlarmIntentResponse")
_INPBSnoozeAlarmIntent = _Class("_INPBSnoozeAlarmIntent")
_INPBCreateAlarmIntent = _Class("_INPBCreateAlarmIntent")
_INPBUpdateAlarmIntent = _Class("_INPBUpdateAlarmIntent")
_INPBAlarmSearch = _Class("_INPBAlarmSearch")
_INPBConnectedCall = _Class("_INPBConnectedCall")
_INPBWholeHouseAudioMetadata = _Class("_INPBWholeHouseAudioMetadata")
_INPBPrivateSearchForMediaIntentData = _Class("_INPBPrivateSearchForMediaIntentData")
_INPBOpenSettingIntent = _Class("_INPBOpenSettingIntent")
_INPBOpenSettingIntentResponse = _Class("_INPBOpenSettingIntentResponse")
_INPBSaveParkingLocationIntent = _Class("_INPBSaveParkingLocationIntent")
_INPBDeleteParkingLocationIntent = _Class("_INPBDeleteParkingLocationIntent")
_INPBDeleteParkingLocationIntentResponse = _Class(
    "_INPBDeleteParkingLocationIntentResponse"
)
_INPBSaveParkingLocationIntentResponse = _Class(
    "_INPBSaveParkingLocationIntentResponse"
)
_INPBSetLabeledSettingIntent = _Class("_INPBSetLabeledSettingIntent")
_INPBSetNumericSettingIntentResponse = _Class("_INPBSetNumericSettingIntentResponse")
_INPBSetBinarySettingIntent = _Class("_INPBSetBinarySettingIntent")
_INPBGetSettingIntentResponse = _Class("_INPBGetSettingIntentResponse")
_INPBNumericSettingValue = _Class("_INPBNumericSettingValue")
_INPBSetNumericSettingIntent = _Class("_INPBSetNumericSettingIntent")
_INPBGetSettingIntent = _Class("_INPBGetSettingIntent")
_INPBSettingMetadata = _Class("_INPBSettingMetadata")
_INPBSetTemporalSettingIntent = _Class("_INPBSetTemporalSettingIntent")
_INPBSetTemporalSettingIntentResponse = _Class("_INPBSetTemporalSettingIntentResponse")
_INPBDevice = _Class("_INPBDevice")
_INPBGetSettingResponseData = _Class("_INPBGetSettingResponseData")
_INPBSetBinarySettingIntentResponse = _Class("_INPBSetBinarySettingIntentResponse")
_INPBSetLabeledSettingIntentResponse = _Class("_INPBSetLabeledSettingIntentResponse")
_INPBPrivateUpdateMediaAffinityIntentData = _Class(
    "_INPBPrivateUpdateMediaAffinityIntentData"
)
_INPBPrivateAddMediaIntentData = _Class("_INPBPrivateAddMediaIntentData")
_INPBPrivateMediaIntentData = _Class("_INPBPrivateMediaIntentData")
_INPBSpeakerIDInfo = _Class("_INPBSpeakerIDInfo")
_INPBMediaSubItem = _Class("_INPBMediaSubItem")
_INPBBoatTrip = _Class("_INPBBoatTrip")
_INPBBusTrip = _Class("_INPBBusTrip")
_INPBPrivatePlayMediaIntentData = _Class("_INPBPrivatePlayMediaIntentData")
_INPBStopShareETAIntentResponse = _Class("_INPBStopShareETAIntentResponse")
_INPBShareETAIntent = _Class("_INPBShareETAIntent")
_INPBShareETAIntentResponse = _Class("_INPBShareETAIntentResponse")
_INPBStopShareETAIntent = _Class("_INPBStopShareETAIntent")
_INPBPrivateMediaItemValueData = _Class("_INPBPrivateMediaItemValueData")
_INPBRetrieveParkingLocationIntent = _Class("_INPBRetrieveParkingLocationIntent")
_INPBRetrieveParkingLocationIntentResponse = _Class(
    "_INPBRetrieveParkingLocationIntentResponse"
)
_INPBSetNicknameIntentResponse = _Class("_INPBSetNicknameIntentResponse")
_INPBSearchForContactIntent = _Class("_INPBSearchForContactIntent")
_INPBSearchForMeCardIntentResponse = _Class("_INPBSearchForMeCardIntentResponse")
_INPBSetRelationshipIntentResponse = _Class("_INPBSetRelationshipIntentResponse")
_INPBSetNicknameIntent = _Class("_INPBSetNicknameIntent")
_INPBSearchForMeCardIntent = _Class("_INPBSearchForMeCardIntent")
_INPBSearchForContactIntentResponse = _Class("_INPBSearchForContactIntentResponse")
_INPBSetRelationshipIntent = _Class("_INPBSetRelationshipIntent")
_INPBColor = _Class("_INPBColor")
_INPBCar = _Class("_INPBCar")
_INPBListCarsIntentResponse = _Class("_INPBListCarsIntentResponse")
_INPBListCarsIntent = _Class("_INPBListCarsIntent")
_INPBDeviceDetail = _Class("_INPBDeviceDetail")
_INPBFindDeviceAndPlaySoundIntent = _Class("_INPBFindDeviceAndPlaySoundIntent")
_INPBFindDeviceAndPlaySoundIntentResponse = _Class(
    "_INPBFindDeviceAndPlaySoundIntentResponse"
)
_INPBMediaItemGroup = _Class("_INPBMediaItemGroup")
_INPBPlayMessageSoundIntent = _Class("_INPBPlayMessageSoundIntent")
_INPBPlayMessageSoundIntentResponse = _Class("_INPBPlayMessageSoundIntentResponse")
_INPBHomeAttributeRange = _Class("_INPBHomeAttributeRange")
_INPBConfidenceScore = _Class("_INPBConfidenceScore")
_INPBConfidenceScoreComponent = _Class("_INPBConfidenceScoreComponent")
_INPBReservationAction = _Class("_INPBReservationAction")
_INPBAirportGate = _Class("_INPBAirportGate")
_INPBShortcutOverview = _Class("_INPBShortcutOverview")
_INPBListShortcutsIntentResponse = _Class("_INPBListShortcutsIntentResponse")
_INPBListShortcutsIntent = _Class("_INPBListShortcutsIntent")
_INPBContactCard = _Class("_INPBContactCard")
_INPBGetReservationDetailsIntent = _Class("_INPBGetReservationDetailsIntent")
_INPBGetReservationDetailsIntentResponse = _Class(
    "_INPBGetReservationDetailsIntentResponse"
)
_INPBReservationWrapper = _Class("_INPBReservationWrapper")
_INPBSpeedValue = _Class("_INPBSpeedValue")
_INPBEnergy = _Class("_INPBEnergy")
_INPBVolumeValue = _Class("_INPBVolumeValue")
_INPBMass = _Class("_INPBMass")
_INPBMassValue = _Class("_INPBMassValue")
_INPBSpeed = _Class("_INPBSpeed")
_INPBModifyNickname = _Class("_INPBModifyNickname")
_INPBVolume = _Class("_INPBVolume")
_INPBEnergyValue = _Class("_INPBEnergyValue")
_INPBIntent = _Class("_INPBIntent")
_INPBIntentExecutionResult = _Class("_INPBIntentExecutionResult")
_INPBFileDataAttachment = _Class("_INPBFileDataAttachment")
_INPBDeleteTasksIntentResponse = _Class("_INPBDeleteTasksIntentResponse")
_INPBSnoozeTasksIntentResponse = _Class("_INPBSnoozeTasksIntentResponse")
_INPBDeleteTasksIntent = _Class("_INPBDeleteTasksIntent")
_INPBSnoozeTasksIntent = _Class("_INPBSnoozeTasksIntent")
_INPBIntentExecutionRequest = _Class("_INPBIntentExecutionRequest")
_INPBPayloadNeedsExecuteIntent = _Class("_INPBPayloadNeedsExecuteIntent")
_INPBAppIdentifier = _Class("_INPBAppIdentifier")
_INPBRestaurantReservation = _Class("_INPBRestaurantReservation")
_INPBRentalCar = _Class("_INPBRentalCar")
_INPBTicketedEvent = _Class("_INPBTicketedEvent")
_INPBLodgingReservation = _Class("_INPBLodgingReservation")
_INPBTrainReservation = _Class("_INPBTrainReservation")
_INPBTicketedEventReservation = _Class("_INPBTicketedEventReservation")
_INPBRentalCarReservation = _Class("_INPBRentalCarReservation")
_INPBTrainTrip = _Class("_INPBTrainTrip")
_INPBContactEventTrigger = _Class("_INPBContactEventTrigger")
_INPBScoredValue = _Class("_INPBScoredValue")
_INPBShowHomeIntent = _Class("_INPBShowHomeIntent")
_INPBShowHomeIntentResponse = _Class("_INPBShowHomeIntentResponse")
_INPBReservation = _Class("_INPBReservation")
_INPBAirline = _Class("_INPBAirline")
_INPBFlight = _Class("_INPBFlight")
_INPBFlightReservation = _Class("_INPBFlightReservation")
_INPBAirport = _Class("_INPBAirport")
_INPBSeat = _Class("_INPBSeat")
_INPBStartCallIntentResponse = _Class("_INPBStartCallIntentResponse")
_INPBHangUpCallIntent = _Class("_INPBHangUpCallIntent")
_INPBHangUpCallIntentResponse = _Class("_INPBHangUpCallIntentResponse")
_INPBStartCallIntent = _Class("_INPBStartCallIntent")
_INPBAnswerCallIntentResponse = _Class("_INPBAnswerCallIntentResponse")
_INPBIdentifyIncomingCallerIntent = _Class("_INPBIdentifyIncomingCallerIntent")
_INPBIdentifyIncomingCallerIntentResponse = _Class(
    "_INPBIdentifyIncomingCallerIntentResponse"
)
_INPBAnswerCallIntent = _Class("_INPBAnswerCallIntent")
_INPBHomeUserTask = _Class("_INPBHomeUserTask")
_INPBHomeUserTaskResponse = _Class("_INPBHomeUserTaskResponse")
_INPBHomeEntityResponse = _Class("_INPBHomeEntityResponse")
_INPBVoiceCommandStepInfo = _Class("_INPBVoiceCommandStepInfo")
_INPBMediaDestination = _Class("_INPBMediaDestination")
_INPBSearchForMediaIntentResponse = _Class("_INPBSearchForMediaIntentResponse")
_INPBSearchForMediaIntent = _Class("_INPBSearchForMediaIntent")
_INPBAddMediaIntentResponse = _Class("_INPBAddMediaIntentResponse")
_INPBAddMediaIntent = _Class("_INPBAddMediaIntent")
_INPBUpdateMediaAffinityIntent = _Class("_INPBUpdateMediaAffinityIntent")
_INPBUpdateMediaAffinityIntentResponse = _Class(
    "_INPBUpdateMediaAffinityIntentResponse"
)
_INPBMediaSearch = _Class("_INPBMediaSearch")
_INPBResetTimerIntent = _Class("_INPBResetTimerIntent")
_INPBCreateTimerIntent = _Class("_INPBCreateTimerIntent")
_INPBCreateTimerIntentResponse = _Class("_INPBCreateTimerIntentResponse")
_INPBMessageLinkMetadata = _Class("_INPBMessageLinkMetadata")
_INPBSetTimerAttributeIntent = _Class("_INPBSetTimerAttributeIntent")
_INPBMediaItemValue = _Class("_INPBMediaItemValue")
_INPBSearchForTimersIntent = _Class("_INPBSearchForTimersIntent")
_INPBSetSeatSettingsInCarIntent = _Class("_INPBSetSeatSettingsInCarIntent")
_INPBEndWorkoutIntent = _Class("_INPBEndWorkoutIntent")
_INPBPair = _Class("_INPBPair")
_INPBPlatformSupport = _Class("_INPBPlatformSupport")
_INPBCallMetrics = _Class("_INPBCallMetrics")
_INPBURLValue = _Class("_INPBURLValue")
_INPBQueryHomeIntent = _Class("_INPBQueryHomeIntent")
_INPBGenericIntentResponse = _Class("_INPBGenericIntentResponse")
_INPBRangeValue = _Class("_INPBRangeValue")
_INPBSetCarLockStatusIntentResponse = _Class("_INPBSetCarLockStatusIntentResponse")
_INPBIntentSlotValue = _Class("_INPBIntentSlotValue")
_INPBSearchForTimersIntentResponse = _Class("_INPBSearchForTimersIntentResponse")
_INPBCallRecordValue = _Class("_INPBCallRecordValue")
_INPBPauseTimerIntentResponse = _Class("_INPBPauseTimerIntentResponse")
_INPBSearchForBillsIntentResponse = _Class("_INPBSearchForBillsIntentResponse")
_INPBEmpty = _Class("_INPBEmpty")
_INPBSetProfileInCarIntentResponse = _Class("_INPBSetProfileInCarIntentResponse")
_INPBSaveProfileInCarIntentResponse = _Class("_INPBSaveProfileInCarIntentResponse")
_INPBNoteContent = _Class("_INPBNoteContent")
_INPBProperty = _Class("_INPBProperty")
_INPBContactRelationship = _Class("_INPBContactRelationship")
_INPBIntentType = _Class("_INPBIntentType")
_INPBEvent = _Class("_INPBEvent")
_INPBPayloadSuccess = _Class("_INPBPayloadSuccess")
_INPBAddTasksIntentResponse = _Class("_INPBAddTasksIntentResponse")
_INPBSetMessageAttributeIntent = _Class("_INPBSetMessageAttributeIntent")
_INPBActivateCarSignalIntentResponse = _Class("_INPBActivateCarSignalIntentResponse")
_INPBDoubleList = _Class("_INPBDoubleList")
_INPBRequestPaymentIntentResponse = _Class("_INPBRequestPaymentIntentResponse")
_INPBUserActivity = _Class("_INPBUserActivity")
_INPBImageValue = _Class("_INPBImageValue")
_INPBStartWorkoutIntent = _Class("_INPBStartWorkoutIntent")
_INPBPauseWorkoutIntentResponse = _Class("_INPBPauseWorkoutIntentResponse")
_INPBConfigureHomeIntentResponse = _Class("_INPBConfigureHomeIntentResponse")
_INPBIntentSlotResolutionResult = _Class("_INPBIntentSlotResolutionResult")
_INPBLocationValue = _Class("_INPBLocationValue")
_INPBPayBillIntentResponse = _Class("_INPBPayBillIntentResponse")
_INPBSearchForBillsIntent = _Class("_INPBSearchForBillsIntent")
_INPBSearchForNotebookItemsIntent = _Class("_INPBSearchForNotebookItemsIntent")
_INPBAppendToNoteIntent = _Class("_INPBAppendToNoteIntent")
_INPBLocalTime = _Class("_INPBLocalTime")
_INPBDistanceValue = _Class("_INPBDistanceValue")
_INPBIntentSlotVocabularyValue = _Class("_INPBIntentSlotVocabularyValue")
_INPBDistanceList = _Class("_INPBDistanceList")
_INPBWellnessObjectResultValue = _Class("_INPBWellnessObjectResultValue")
_INPBStartAudioCallIntent = _Class("_INPBStartAudioCallIntent")
_INPBTransferMoneyIntentResponse = _Class("_INPBTransferMoneyIntentResponse")
_INPBDialingContactValue = _Class("_INPBDialingContactValue")
_INPBSendPaymentIntentResponse = _Class("_INPBSendPaymentIntentResponse")
_INPBLong = _Class("_INPBLong")
_INPBRequestRideIntent = _Class("_INPBRequestRideIntent")
_INPBTemperatureList = _Class("_INPBTemperatureList")
_INPBActivityList = _Class("_INPBActivityList")
_INPBLongList = _Class("_INPBLongList")
_INPBNote = _Class("_INPBNote")
_INPBWellnessValue = _Class("_INPBWellnessValue")
_INPBRidePartySizeOption = _Class("_INPBRidePartySizeOption")
_INPBTask = _Class("_INPBTask")
_INPBStringList = _Class("_INPBStringList")
_INPBRunVoiceCommandIntent = _Class("_INPBRunVoiceCommandIntent")
_INPBGeographicalFeatureList = _Class("_INPBGeographicalFeatureList")
_INPBDateTimeRangeValue = _Class("_INPBDateTimeRangeValue")
_INPBSearchForNotebookItemsIntentResponse = _Class(
    "_INPBSearchForNotebookItemsIntentResponse"
)
_INPBBuildId = _Class("_INPBBuildId")
_INPBSetRadioStationIntent = _Class("_INPBSetRadioStationIntent")
_INPBFinancialAccountValue = _Class("_INPBFinancialAccountValue")
_INPBCondition = _Class("_INPBCondition")
_INPBRunVoiceCommandIntentResponse = _Class("_INPBRunVoiceCommandIntentResponse")
_INPBLocationList = _Class("_INPBLocationList")
_INPBPauseWorkoutIntent = _Class("_INPBPauseWorkoutIntent")
_INPBQueryHomeIntentResponse = _Class("_INPBQueryHomeIntentResponse")
_INPBCurrencyAmountValue = _Class("_INPBCurrencyAmountValue")
_INPBCreateTaskListIntent = _Class("_INPBCreateTaskListIntent")
_INPBSearchForAccountsIntentResponse = _Class("_INPBSearchForAccountsIntentResponse")
_INPBPlace = _Class("_INPBPlace")
_INPBSaveHealthSampleIntent = _Class("_INPBSaveHealthSampleIntent")
_INPBResumeWorkoutIntent = _Class("_INPBResumeWorkoutIntent")
_INPBIntentResponsePayloadFailure = _Class("_INPBIntentResponsePayloadFailure")
_INPBArchivedObject = _Class("_INPBArchivedObject")
_INPBPauseTimerIntent = _Class("_INPBPauseTimerIntent")
_INPBAppendToNoteIntentResponse = _Class("_INPBAppendToNoteIntentResponse")
_INPBCopyFileIntent = _Class("_INPBCopyFileIntent")
_INPBShareDestination = _Class("_INPBShareDestination")
_INPBSearchCallHistoryIntent = _Class("_INPBSearchCallHistoryIntent")
_INPBMoveFileIntentResponse = _Class("_INPBMoveFileIntentResponse")
_INPBAppNames = _Class("_INPBAppNames")
_INPBActivity = _Class("_INPBActivity")
_INPBTemporalEventTrigger = _Class("_INPBTemporalEventTrigger")
_INPBPayloadUnsupported = _Class("_INPBPayloadUnsupported")
_INPBCompressFileIntent = _Class("_INPBCompressFileIntent")
_INPBResetTimerIntentResponse = _Class("_INPBResetTimerIntentResponse")
_INPBRideCompletionStatus = _Class("_INPBRideCompletionStatus")
_INPBPlayMediaIntent = _Class("_INPBPlayMediaIntent")
_INPBGetCarPowerLevelStatusIntent = _Class("_INPBGetCarPowerLevelStatusIntent")
_INPBHomeAttribute = _Class("_INPBHomeAttribute")
_INPBCreateNoteIntentResponse = _Class("_INPBCreateNoteIntentResponse")
_INPBStartAudioCallIntentResponse = _Class("_INPBStartAudioCallIntentResponse")
_INPBPayloadNeedsDisambiguation = _Class("_INPBPayloadNeedsDisambiguation")
_INPBSetMessageAttributeIntentResponse = _Class(
    "_INPBSetMessageAttributeIntentResponse"
)
_INPBRideOption = _Class("_INPBRideOption")
_INPBGetFileInformationIntent = _Class("_INPBGetFileInformationIntent")
_INPBSaveHealthSampleIntentResponse = _Class("_INPBSaveHealthSampleIntentResponse")
_INPBRideStatus = _Class("_INPBRideStatus")
_INPBPaymentAmountValue = _Class("_INPBPaymentAmountValue")
_INPBSaveProfileInCarIntent = _Class("_INPBSaveProfileInCarIntent")
_INPBEndWorkoutIntentResponse = _Class("_INPBEndWorkoutIntentResponse")
_INPBRecurrenceValue = _Class("_INPBRecurrenceValue")
_INPBPayBillIntent = _Class("_INPBPayBillIntent")
_INPBContactList = _Class("_INPBContactList")
_INPBSendMessageIntent = _Class("_INPBSendMessageIntent")
_INPBSearchForFilesIntentResponse = _Class("_INPBSearchForFilesIntentResponse")
_INPBTimer = _Class("_INPBTimer")
_INPBIntentSlotVocabularyPolicy = _Class("_INPBIntentSlotVocabularyPolicy")
_INPBSetRadioStationIntentResponse = _Class("_INPBSetRadioStationIntentResponse")
_INPBLocalDate = _Class("_INPBLocalDate")
_INPBSetAudioSourceInCarIntentResponse = _Class(
    "_INPBSetAudioSourceInCarIntentResponse"
)
_INPBPlaceList = _Class("_INPBPlaceList")
_INPBSetSeatSettingsInCarIntentResponse = _Class(
    "_INPBSetSeatSettingsInCarIntentResponse"
)
_INPBWellnessUnitType = _Class("_INPBWellnessUnitType")
_INPBDateTimeRangeList = _Class("_INPBDateTimeRangeList")
_INPBLanguageTag = _Class("_INPBLanguageTag")
_INPBLocation = _Class("_INPBLocation")
_INPBSelectionItem = _Class("_INPBSelectionItem")
_INPBCreateFileIntentResponse = _Class("_INPBCreateFileIntentResponse")
_INPBDateTime = _Class("_INPBDateTime")
_INPBCompressFileIntentResponse = _Class("_INPBCompressFileIntentResponse")
_INPBListRideOptionsIntent = _Class("_INPBListRideOptionsIntent")
_INPBScanVisualCodeIntentResponse = _Class("_INPBScanVisualCodeIntentResponse")
_INPBPlayMediaIntentResponse = _Class("_INPBPlayMediaIntentResponse")
_INPBSetCarLockStatusIntent = _Class("_INPBSetCarLockStatusIntent")
_INPBDoubleValue = _Class("_INPBDoubleValue")
_INPBCancelWorkoutIntent = _Class("_INPBCancelWorkoutIntent")
_INPBCurrencyAmount = _Class("_INPBCurrencyAmount")
_INPBBoolValue = _Class("_INPBBoolValue")
_INPBBalanceAmountValue = _Class("_INPBBalanceAmountValue")
_INPBDeleteFilePermanentlyIntent = _Class("_INPBDeleteFilePermanentlyIntent")
_INPBPayloadConfirmation = _Class("_INPBPayloadConfirmation")
_INPBSearchForPhotosIntentResponse = _Class("_INPBSearchForPhotosIntentResponse")
_INPBAddTasksIntent = _Class("_INPBAddTasksIntent")
_INPBResumeTimerIntent = _Class("_INPBResumeTimerIntent")
_INPBPlayVoicemailIntentResponse = _Class("_INPBPlayVoicemailIntentResponse")
_INPBRideDriver = _Class("_INPBRideDriver")
_INPBListRideOptionsIntentResponse = _Class("_INPBListRideOptionsIntentResponse")
_INPBRequestRideIntentResponse = _Class("_INPBRequestRideIntentResponse")
_INPBSetClimateSettingsInCarIntent = _Class("_INPBSetClimateSettingsInCarIntent")
_INPBScanVisualCodeIntent = _Class("_INPBScanVisualCodeIntent")
_INPBCreateFileIntent = _Class("_INPBCreateFileIntent")
_INPBBillDetailsValue = _Class("_INPBBillDetailsValue")
_INPBDistance = _Class("_INPBDistance")
_INPBIntegerList = _Class("_INPBIntegerList")
_INPBIntentResponse = _Class("_INPBIntentResponse")
_INPBSetAudioSourceInCarIntent = _Class("_INPBSetAudioSourceInCarIntent")
_INPBPaymentMethodValue = _Class("_INPBPaymentMethodValue")
_INPBResumeWorkoutIntentResponse = _Class("_INPBResumeWorkoutIntentResponse")
_INPBPaymentMethod = _Class("_INPBPaymentMethod")
_INPBCopyFileIntentResponse = _Class("_INPBCopyFileIntentResponse")
_INPBResumeTimerIntentResponse = _Class("_INPBResumeTimerIntentResponse")
_INPBDialingContact = _Class("_INPBDialingContact")
_INPBDictionary = _Class("_INPBDictionary")
_INPBCreateTaskListIntentResponse = _Class("_INPBCreateTaskListIntentResponse")
_INPBSearchForAccountsIntent = _Class("_INPBSearchForAccountsIntent")
_INPBEventList = _Class("_INPBEventList")
_INPBSendMessageIntentResponse = _Class("_INPBSendMessageIntentResponse")
_INPBSetClimateSettingsInCarIntentResponse = _Class(
    "_INPBSetClimateSettingsInCarIntentResponse"
)
_INPBSearchForPhotosIntent = _Class("_INPBSearchForPhotosIntent")
_INPBDeleteFilePermanentlyIntentResponse = _Class(
    "_INPBDeleteFilePermanentlyIntentResponse"
)
_INPBInteger = _Class("_INPBInteger")
_INPBRequestPaymentIntent = _Class("_INPBRequestPaymentIntent")
_INPBUncompressFileIntent = _Class("_INPBUncompressFileIntent")
_INPBWellnessMetadataPair = _Class("_INPBWellnessMetadataPair")
_INPBUUIDValue = _Class("_INPBUUIDValue")
_INPBConflictingParameter = _Class("_INPBConflictingParameter")
_INPBStartVideoCallIntentResponse = _Class("_INPBStartVideoCallIntentResponse")
_INPBFileProperty = _Class("_INPBFileProperty")
_INPBStringValue = _Class("_INPBStringValue")
_INPBRefinementItem = _Class("_INPBRefinementItem")
_INPBSetDefrosterSettingsInCarIntent = _Class("_INPBSetDefrosterSettingsInCarIntent")
_INPBTemperature = _Class("_INPBTemperature")
_INPBCancelWorkoutIntentResponse = _Class("_INPBCancelWorkoutIntentResponse")
_INPBSpatialEventTrigger = _Class("_INPBSpatialEventTrigger")
_INPBPlayAudioMessageIntent = _Class("_INPBPlayAudioMessageIntent")
_INPBDeleteHealthSampleIntent = _Class("_INPBDeleteHealthSampleIntent")
_INPBGetFileInformationIntentResponse = _Class("_INPBGetFileInformationIntentResponse")
_INPBSetTimerAttributeIntentResponse = _Class("_INPBSetTimerAttributeIntentResponse")
_INPBDuration = _Class("_INPBDuration")
_INPBPriceRangeValue = _Class("_INPBPriceRangeValue")
_INPBMoveFileIntent = _Class("_INPBMoveFileIntent")
_INPBTimestamp = _Class("_INPBTimestamp")
_INPBStartPhotoPlaybackIntent = _Class("_INPBStartPhotoPlaybackIntent")
_INPBModifyRelationship = _Class("_INPBModifyRelationship")
_INPBPlayVoicemailIntent = _Class("_INPBPlayVoicemailIntent")
_INPBDeleteTimerIntent = _Class("_INPBDeleteTimerIntent")
_INPBImageNoteContent = _Class("_INPBImageNoteContent")
_INPBGetRideStatusIntent = _Class("_INPBGetRideStatusIntent")
_INPBIntentSupport = _Class("_INPBIntentSupport")
_INPBControlHomeIntent = _Class("_INPBControlHomeIntent")
_INPBSetDefrosterSettingsInCarIntentResponse = _Class(
    "_INPBSetDefrosterSettingsInCarIntentResponse"
)
_INPBTemperatureValue = _Class("_INPBTemperatureValue")
_INPBTextNoteContent = _Class("_INPBTextNoteContent")
_INPBSearchForMessagesIntent = _Class("_INPBSearchForMessagesIntent")
_INPBSetTaskAttributeIntentResponse = _Class("_INPBSetTaskAttributeIntentResponse")
_INPBRideVehicle = _Class("_INPBRideVehicle")
_INPBContactValue = _Class("_INPBContactValue")
_INPBWellnessMetadataValue = _Class("_INPBWellnessMetadataValue")
_INPBStartVideoCallIntent = _Class("_INPBStartVideoCallIntent")
_INPBString = _Class("_INPBString")
_INPBContactHandle = _Class("_INPBContactHandle")
_INPBSetProfileInCarIntent = _Class("_INPBSetProfileInCarIntent")
_INPBDecimalNumberValue = _Class("_INPBDecimalNumberValue")
_INPBStartWorkoutIntentResponse = _Class("_INPBStartWorkoutIntentResponse")
_INPBOpenFileIntentResponse = _Class("_INPBOpenFileIntentResponse")
_INPBShareFileIntentResponse = _Class("_INPBShareFileIntentResponse")
_INPBIntentTypePhrases = _Class("_INPBIntentTypePhrases")
_INPBControlHomeIntentResponse = _Class("_INPBControlHomeIntentResponse")
_INPBDeleteHealthSampleIntentResponse = _Class("_INPBDeleteHealthSampleIntentResponse")
_INPBAppBundleInfo = _Class("_INPBAppBundleInfo")
_INPBHomeAttributeValue = _Class("_INPBHomeAttributeValue")
_INPBOpenFileIntent = _Class("_INPBOpenFileIntent")
_INPBPaymentRecord = _Class("_INPBPaymentRecord")
_INPBUncompressFileIntentResponse = _Class("_INPBUncompressFileIntentResponse")
_INPBCallMetricsValue = _Class("_INPBCallMetricsValue")
_INPBPlayAudioMessageIntentResponse = _Class("_INPBPlayAudioMessageIntentResponse")
_INPBFilePropertyValue = _Class("_INPBFilePropertyValue")
_INPBTransferMoneyIntent = _Class("_INPBTransferMoneyIntent")
_INPBQueryHealthSampleIntentResponse = _Class("_INPBQueryHealthSampleIntentResponse")
_INPBSendPaymentIntent = _Class("_INPBSendPaymentIntent")
_INPBIntegerValue = _Class("_INPBIntegerValue")
_INPBDataString = _Class("_INPBDataString")
_INPBLongValue = _Class("_INPBLongValue")
_INPBGetCarLockStatusIntentResponse = _Class("_INPBGetCarLockStatusIntentResponse")
_INPBDeleteTimerIntentResponse = _Class("_INPBDeleteTimerIntentResponse")
_INPBCustomObject = _Class("_INPBCustomObject")
_INPBIntentSlotResolutionMulticardinalResult = _Class(
    "_INPBIntentSlotResolutionMulticardinalResult"
)
_INPBLocalizedProject = _Class("_INPBLocalizedProject")
_INPBSearchForFilesIntent = _Class("_INPBSearchForFilesIntent")
_INPBSearchCallHistoryIntentResponse = _Class("_INPBSearchCallHistoryIntentResponse")
_INPBIntentSlotVocabularyConcept = _Class("_INPBIntentSlotVocabularyConcept")
_INPBGetRideStatusIntentResponse = _Class("_INPBGetRideStatusIntentResponse")
_INPBCreateNoteIntent = _Class("_INPBCreateNoteIntent")
_INPBSearchForMessagesIntentResponse = _Class("_INPBSearchForMessagesIntentResponse")
_INPBContact = _Class("_INPBContact")
_INPBTaskList = _Class("_INPBTaskList")
_INPBGetCarPowerLevelStatusIntentResponse = _Class(
    "_INPBGetCarPowerLevelStatusIntentResponse"
)
_INPBQueryHealthSampleIntent = _Class("_INPBQueryHealthSampleIntent")
_INPBStartPhotoPlaybackIntentResponse = _Class("_INPBStartPhotoPlaybackIntentResponse")
_INPBRideFareLineItem = _Class("_INPBRideFareLineItem")
_INPBMessage = _Class("_INPBMessage")
_INPBGetVisualCodeIntent = _Class("_INPBGetVisualCodeIntent")
_INPBGetCarLockStatusIntent = _Class("_INPBGetCarLockStatusIntent")
_INPBAppId = _Class("_INPBAppId")
_INPBGetVisualCodeIntentResponse = _Class("_INPBGetVisualCodeIntentResponse")
_INPBGeographicalFeature = _Class("_INPBGeographicalFeature")
_INPBValueMetadata = _Class("_INPBValueMetadata")
_INPBIntentResponsePayloadSuccess = _Class("_INPBIntentResponsePayloadSuccess")
_INPBActivateCarSignalIntent = _Class("_INPBActivateCarSignalIntent")
_INPBHomeEntity = _Class("_INPBHomeEntity")
_INPBSendMessageAttachment = _Class("_INPBSendMessageAttachment")
_INPBRunWorkflowIntentResponse = _Class("_INPBRunWorkflowIntentResponse")
_INPBDateTimeRange = _Class("_INPBDateTimeRange")
_INPBIntentVocabulary = _Class("_INPBIntentVocabulary")
_INPBVoiceCommandDeviceInformation = _Class("_INPBVoiceCommandDeviceInformation")
_INPBDouble = _Class("_INPBDouble")
_INPBDataStringList = _Class("_INPBDataStringList")
_INPBAppBuild = _Class("_INPBAppBuild")
_INPBShareFileIntent = _Class("_INPBShareFileIntent")
_INPBRunWorkflowIntent = _Class("_INPBRunWorkflowIntent")
_INPBHomeFilter = _Class("_INPBHomeFilter")
_INPBHomeContent = _Class("_INPBHomeContent")
_INPBPaymentMethodList = _Class("_INPBPaymentMethodList")
_INPBPayloadNeedsValue = _Class("_INPBPayloadNeedsValue")
_INPBConfigureHomeIntent = _Class("_INPBConfigureHomeIntent")
_INPBSetTaskAttributeIntent = _Class("_INPBSetTaskAttributeIntent")
_INPBBillPayeeValue = _Class("_INPBBillPayeeValue")
_INPBBool = _Class("_INPBBool")
_INPBFile = _Class("_INPBFile")
_INPBGenericIntent = _Class("_INPBGenericIntent")
INCodable = _Class("INCodable")
_INPBIntentMetadata = _Class("_INPBIntentMetadata")
INIntentCarHeadUnitSlotValueTransformer = _Class(
    "INIntentCarHeadUnitSlotValueTransformer"
)
INIntentCarChargingConnectorPowerSlotValueTransformer = _Class(
    "INIntentCarChargingConnectorPowerSlotValueTransformer"
)
INIntentCallRecordFilterSlotValueTransformer = _Class(
    "INIntentCallRecordFilterSlotValueTransformer"
)
INIntentBusReservationSlotValueTransformer = _Class(
    "INIntentBusReservationSlotValueTransformer"
)
INIntentBoatReservationSlotValueTransformer = _Class(
    "INIntentBoatReservationSlotValueTransformer"
)
INIntentSleepAlarmAttributeSlotValueTransformer = _Class(
    "INIntentSleepAlarmAttributeSlotValueTransformer"
)
INIntentAlarmSearchSlotValueTransformer = _Class(
    "INIntentAlarmSearchSlotValueTransformer"
)
INIntentAlarmSlotValueTransformer = _Class("INIntentAlarmSlotValueTransformer")
INIntentConnectedCallSlotValueTransformer = _Class(
    "INIntentConnectedCallSlotValueTransformer"
)
INIntentWholeHouseAudioMetadataSlotValueTransformer = _Class(
    "INIntentWholeHouseAudioMetadataSlotValueTransformer"
)
INIntentPrivateSearchForMediaIntentDataSlotValueTransformer = _Class(
    "INIntentPrivateSearchForMediaIntentDataSlotValueTransformer"
)
INIntentGetSettingResponseDataSlotValueTransformer = _Class(
    "INIntentGetSettingResponseDataSlotValueTransformer"
)
INIntentNumericSettingValueSlotValueTransformer = _Class(
    "INIntentNumericSettingValueSlotValueTransformer"
)
INIntentSettingDeviceSlotValueTransformer = _Class(
    "INIntentSettingDeviceSlotValueTransformer"
)
INIntentSettingMetadataSlotValueTransformer = _Class(
    "INIntentSettingMetadataSlotValueTransformer"
)
INIntentPrivateUpdateMediaAffinityIntentDataSlotValueTransformer = _Class(
    "INIntentPrivateUpdateMediaAffinityIntentDataSlotValueTransformer"
)
INIntentPrivateAddMediaIntentDataSlotValueTransformer = _Class(
    "INIntentPrivateAddMediaIntentDataSlotValueTransformer"
)
INIntentPrivateMediaIntentDataSlotValueTransformer = _Class(
    "INIntentPrivateMediaIntentDataSlotValueTransformer"
)
INIntentSpeakerIDInfoSlotValueTransformer = _Class(
    "INIntentSpeakerIDInfoSlotValueTransformer"
)
INIntentMediaSubItemSlotValueTransformer = _Class(
    "INIntentMediaSubItemSlotValueTransformer"
)
INIntentBoatTripSlotValueTransformer = _Class("INIntentBoatTripSlotValueTransformer")
INIntentBusTripSlotValueTransformer = _Class("INIntentBusTripSlotValueTransformer")
INIntentPrivatePlayMediaIntentDataSlotValueTransformer = _Class(
    "INIntentPrivatePlayMediaIntentDataSlotValueTransformer"
)
INIntentPrivateMediaItemValueDataSlotValueTransformer = _Class(
    "INIntentPrivateMediaItemValueDataSlotValueTransformer"
)
INIntentCarSlotValueTransformer = _Class("INIntentCarSlotValueTransformer")
INIntentDeviceDetailSlotValueTransformer = _Class(
    "INIntentDeviceDetailSlotValueTransformer"
)
INIntentMediaDestinationSlotValueTransformer = _Class(
    "INIntentMediaDestinationSlotValueTransformer"
)
INIntentReservationActionSlotValueTransformer = _Class(
    "INIntentReservationActionSlotValueTransformer"
)
INIntentAirportGateSlotValueTransformer = _Class(
    "INIntentAirportGateSlotValueTransformer"
)
INIntentShortcutOverviewSlotValueTransformer = _Class(
    "INIntentShortcutOverviewSlotValueTransformer"
)
INIntentAppIdentifierSlotValueTransformer = _Class(
    "INIntentAppIdentifierSlotValueTransformer"
)
INIntentReservationWrapperSlotValueTransformer = _Class(
    "INIntentReservationWrapperSlotValueTransformer"
)
INIntentRentalCarSlotValueTransformer = _Class("INIntentRentalCarSlotValueTransformer")
INIntentTicketedEventSlotValueTransformer = _Class(
    "INIntentTicketedEventSlotValueTransformer"
)
INIntentTrainTripSlotValueTransformer = _Class("INIntentTrainTripSlotValueTransformer")
INIntentMediaItemGroupSlotValueTransformer = _Class(
    "INIntentMediaItemGroupSlotValueTransformer"
)
INIntentEnergySlotValueTransformer = _Class("INIntentEnergySlotValueTransformer")
INIntentContactEventTriggerSlotValueTransformer = _Class(
    "INIntentContactEventTriggerSlotValueTransformer"
)
INIntentMediaItemSlotValueTransformer = _Class("INIntentMediaItemSlotValueTransformer")
INIntentAirlineSlotValueTransformer = _Class("INIntentAirlineSlotValueTransformer")
INIntentFlightSlotValueTransformer = _Class("INIntentFlightSlotValueTransformer")
INIntentAirportSlotValueTransformer = _Class("INIntentAirportSlotValueTransformer")
INIntentSeatSlotValueTransformer = _Class("INIntentSeatSlotValueTransformer")
INIntentMessageAttachmentSlotValueTransformer = _Class(
    "INIntentMessageAttachmentSlotValueTransformer"
)
INIntentIntentExecutionResultSlotValueTransformer = _Class(
    "INIntentIntentExecutionResultSlotValueTransformer"
)
INIntentHomeUserTaskResponseSlotValueTransformer = _Class(
    "INIntentHomeUserTaskResponseSlotValueTransformer"
)
INIntentHomeEntityResponseSlotValueTransformer = _Class(
    "INIntentHomeEntityResponseSlotValueTransformer"
)
INIntentHomeUserTaskSlotValueTransformer = _Class(
    "INIntentHomeUserTaskSlotValueTransformer"
)
INIntentVoiceCommandStepInfoSlotValueTransformer = _Class(
    "INIntentVoiceCommandStepInfoSlotValueTransformer"
)
INIntentMediaSearchSlotValueTransformer = _Class(
    "INIntentMediaSearchSlotValueTransformer"
)
INIntentVoiceCommandDeviceInformationSlotValueTransformer = _Class(
    "INIntentVoiceCommandDeviceInformationSlotValueTransformer"
)
INIntentArchivedObjectSlotValueTransformer = _Class(
    "INIntentArchivedObjectSlotValueTransformer"
)
INIntentMessageLinkMetadataSlotValueTransformer = _Class(
    "INIntentMessageLinkMetadataSlotValueTransformer"
)
INIntentHomeFilterSlotValueTransformer = _Class(
    "INIntentHomeFilterSlotValueTransformer"
)
INIntentHomeContentSlotValueTransformer = _Class(
    "INIntentHomeContentSlotValueTransformer"
)
INIntentTimerSlotValueTransformer = _Class("INIntentTimerSlotValueTransformer")
INIntentGeographicalFeatureSlotValueTransformer = _Class(
    "INIntentGeographicalFeatureSlotValueTransformer"
)
INIntentActivitySlotValueTransformer = _Class("INIntentActivitySlotValueTransformer")
INIntentPlaceSlotValueTransformer = _Class("INIntentPlaceSlotValueTransformer")
INIntentEventSlotValueTransformer = _Class("INIntentEventSlotValueTransformer")
INIntentBillPayeeSlotValueTransformer = _Class("INIntentBillPayeeSlotValueTransformer")
INIntentTrainReservationSlotValueTransformer = _Class(
    "INIntentTrainReservationSlotValueTransformer"
)
INIntentDateSlotValueTransformer = _Class("INIntentDateSlotValueTransformer")
INIntentWellnessUnitTypeSlotValueTransformer = _Class(
    "INIntentWellnessUnitTypeSlotValueTransformer"
)
INIntentTaskListSlotValueTransformer = _Class("INIntentTaskListSlotValueTransformer")
INIntentHomeActionSlotValueTransformer = _Class(
    "INIntentHomeActionSlotValueTransformer"
)
INIntentSpeakableStringSlotValueTransformer = _Class(
    "INIntentSpeakableStringSlotValueTransformer"
)
INIntentPlacemarkSlotValueTransformer = _Class("INIntentPlacemarkSlotValueTransformer")
INIntentLocationSlotValueTransformer = _Class("INIntentLocationSlotValueTransformer")
INIntentTaskSlotValueTransformer = _Class("INIntentTaskSlotValueTransformer")
INIntentNoteContentSlotValueTransformer = _Class(
    "INIntentNoteContentSlotValueTransformer"
)
INIntentDistanceSlotValueTransformer = _Class("INIntentDistanceSlotValueTransformer")
INIntentGEOLatLngSlotValueTransformer = _Class("INIntentGEOLatLngSlotValueTransformer")
INIntentWellnessObjectResultValueSlotValueTransformer = _Class(
    "INIntentWellnessObjectResultValueSlotValueTransformer"
)
INIntentNullSlotValueTransformer = _Class("INIntentNullSlotValueTransformer")
INIntentWellnessMetadataPairSlotValueTransformer = _Class(
    "INIntentWellnessMetadataPairSlotValueTransformer"
)
INIntentPaymentRecordSlotValueTransformer = _Class(
    "INIntentPaymentRecordSlotValueTransformer"
)
INIntentTicketedEventReservationSlotValueTransformer = _Class(
    "INIntentTicketedEventReservationSlotValueTransformer"
)
INIntentCurrencyAmountSlotValueTransformer = _Class(
    "INIntentCurrencyAmountSlotValueTransformer"
)
INIntentRentalCarReservationSlotValueTransformer = _Class(
    "INIntentRentalCarReservationSlotValueTransformer"
)
INIntentDictionarySlotValueTransformer = _Class(
    "INIntentDictionarySlotValueTransformer"
)
INIntentBillDetailsSlotValueTransformer = _Class(
    "INIntentBillDetailsSlotValueTransformer"
)
INIntentMessageSlotValueTransformer = _Class("INIntentMessageSlotValueTransformer")
INIntentMassSlotValueTransformer = _Class("INIntentMassSlotValueTransformer")
INIntentSpeedSlotValueTransformer = _Class("INIntentSpeedSlotValueTransformer")
INIntentImageSlotValueTransformer = _Class("INIntentImageSlotValueTransformer")
INIntentIntentSlotValueTransformer = _Class("INIntentIntentSlotValueTransformer")
INIntentDialingContactSlotValueTransformer = _Class(
    "INIntentDialingContactSlotValueTransformer"
)
INIntentPersonSlotValueTransformer = _Class("INIntentPersonSlotValueTransformer")
INIntentRideOptionSlotValueTransformer = _Class(
    "INIntentRideOptionSlotValueTransformer"
)
INIntentContactCardSlotValueTransformer = _Class(
    "INIntentContactCardSlotValueTransformer"
)
INIntentHomeAttributeValueSlotValueTransformer = _Class(
    "INIntentHomeAttributeValueSlotValueTransformer"
)
INIntentTemporalEventTriggerSlotValueTransformer = _Class(
    "INIntentTemporalEventTriggerSlotValueTransformer"
)
INIntentContactRelationshipSlotValueTransformer = _Class(
    "INIntentContactRelationshipSlotValueTransformer"
)
INIntentObjectSlotValueTransformer = _Class("INIntentObjectSlotValueTransformer")
INIntentJSONDictionarySlotValueTransformer = _Class(
    "INIntentJSONDictionarySlotValueTransformer"
)
INIntentDoubleSlotValueTransformer = _Class("INIntentDoubleSlotValueTransformer")
INIntentCallRecordSlotValueTransformer = _Class(
    "INIntentCallRecordSlotValueTransformer"
)
INIntentModifyRelationshipSlotValueTransformer = _Class(
    "INIntentModifyRelationshipSlotValueTransformer"
)
INIntentURLSlotValueTransformer = _Class("INIntentURLSlotValueTransformer")
INIntentUUIDSlotValueTransformer = _Class("INIntentUUIDSlotValueTransformer")
INIntentDateComponentsRangeSlotValueTransformer = _Class(
    "INIntentDateComponentsRangeSlotValueTransformer"
)
INIntentBalanceAmountSlotValueTransformer = _Class(
    "INIntentBalanceAmountSlotValueTransformer"
)
INIntentPaymentMethodSlotValueTransformer = _Class(
    "INIntentPaymentMethodSlotValueTransformer"
)
INIntentVolumeSlotValueTransformer = _Class("INIntentVolumeSlotValueTransformer")
INIntentSpatialEventTriggerSlotValueTransformer = _Class(
    "INIntentSpatialEventTriggerSlotValueTransformer"
)
INIntentFlightReservationSlotValueTransformer = _Class(
    "INIntentFlightReservationSlotValueTransformer"
)
INIntentRideStatusSlotValueTransformer = _Class(
    "INIntentRideStatusSlotValueTransformer"
)
INIntentRestaurantReservationSlotValueTransformer = _Class(
    "INIntentRestaurantReservationSlotValueTransformer"
)
INIntentDateComponentsSlotValueTransformer = _Class(
    "INIntentDateComponentsSlotValueTransformer"
)
INIntentWellnessValueSlotValueTransformer = _Class(
    "INIntentWellnessValueSlotValueTransformer"
)
INIntentNoteSlotValueTransformer = _Class("INIntentNoteSlotValueTransformer")
INIntentPowerSlotValueTransformer = _Class("INIntentPowerSlotValueTransformer")
INIntentHomeAttributeSlotValueTransformer = _Class(
    "INIntentHomeAttributeSlotValueTransformer"
)
INIntentDecimalNumberSlotValueTransformer = _Class(
    "INIntentDecimalNumberSlotValueTransformer"
)
INIntentTemperatureSlotValueTransformer = _Class(
    "INIntentTemperatureSlotValueTransformer"
)
INIntentHomeEntitySlotValueTransformer = _Class(
    "INIntentHomeEntitySlotValueTransformer"
)
INIntentStringSlotValueTransformer = _Class("INIntentStringSlotValueTransformer")
INIntentLodgingReservationSlotValueTransformer = _Class(
    "INIntentLodgingReservationSlotValueTransformer"
)
INIntentModifyNicknameSlotValueTransformer = _Class(
    "INIntentModifyNicknameSlotValueTransformer"
)
INIntentPaymentAmountSlotValueTransformer = _Class(
    "INIntentPaymentAmountSlotValueTransformer"
)
INIntentLongSlotValueTransformer = _Class("INIntentLongSlotValueTransformer")
INIntentIntegerSlotValueTransformer = _Class("INIntentIntegerSlotValueTransformer")
INIntentPaymentAccountSlotValueTransformer = _Class(
    "INIntentPaymentAccountSlotValueTransformer"
)
INIntentBooleanSlotValueTransformer = _Class("INIntentBooleanSlotValueTransformer")
INIntentFileSlotValueTransformer = _Class("INIntentFileSlotValueTransformer")
_INCodableAttributeRelationshipValueTransformer = _Class(
    "_INCodableAttributeRelationshipValueTransformer"
)
_INCodableScalarAttributeRelationshipStringValueTransformer = _Class(
    "_INCodableScalarAttributeRelationshipStringValueTransformer"
)
_INCodableObjectAttributeRelationshipNumberValueTransformer = _Class(
    "_INCodableObjectAttributeRelationshipNumberValueTransformer"
)
_INCodableEnumAttributeRelationshipValueTransformer = _Class(
    "_INCodableEnumAttributeRelationshipValueTransformer"
)
INExtensionContextHost = _Class("INExtensionContextHost")
_INExtensionContext = _Class("_INExtensionContext")
INResolutionResultTransformationOperation = _Class(
    "INResolutionResultTransformationOperation"
)
INImageProxyInjectionOperation = _Class("INImageProxyInjectionOperation")
INDeferredLocalizedString = _Class("INDeferredLocalizedString")
